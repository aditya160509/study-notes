#!/usr/bin/env python3
import json
import subprocess
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


MODEL = "deepseek-v4-flash-free"
OPENCODE_MODEL = f"opencode/{MODEL}"


def _message_text(message):
    content = message.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
        return "\n".join(parts)
    return str(content)


def _prompt_from_messages(messages):
    chunks = []
    for message in messages:
        role = message.get("role", "user")
        text = _message_text(message).strip()
        if text:
            chunks.append(f"{role.upper()}:\n{text}")
    return "\n\n".join(chunks)


def _run_opencode(prompt):
    cmd = [
        "opencode",
        "run",
        "-m",
        OPENCODE_MODEL,
        "--format",
        "json",
        prompt,
    ]
    proc = subprocess.run(
        cmd,
        cwd="/Users/adityabalaji/Documents/Codex/2026-08-14/i",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=240,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "opencode failed")
    texts = []
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "text":
            part = event.get("part") or {}
            texts.append(part.get("text", ""))
    return "".join(texts).strip()


class Handler(BaseHTTPRequestHandler):
    server_version = "opencode-hermes-bridge/0.1"

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/v1/models":
            return self._send_json(200, {
                "object": "list",
                "data": [{"id": MODEL, "object": "model", "owned_by": "opencode-bridge"}],
            })
        return self._send_json(404, {"error": {"message": "not found"}})

    def do_POST(self):
        if self.path != "/v1/chat/completions":
            return self._send_json(404, {"error": {"message": "not found"}})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            request = json.loads(self.rfile.read(length) or b"{}")
            prompt = _prompt_from_messages(request.get("messages", []))
            answer = _run_opencode(prompt)
            created = int(time.time())
            completion_id = "chatcmpl-" + uuid.uuid4().hex
            if request.get("stream"):
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                chunk = {
                    "id": completion_id,
                    "object": "chat.completion.chunk",
                    "created": created,
                    "model": MODEL,
                    "choices": [{"index": 0, "delta": {"content": answer}, "finish_reason": None}],
                }
                self.wfile.write(f"data: {json.dumps(chunk)}\n\n".encode())
                done = {
                    "id": completion_id,
                    "object": "chat.completion.chunk",
                    "created": created,
                    "model": MODEL,
                    "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
                }
                self.wfile.write(f"data: {json.dumps(done)}\n\n".encode())
                self.wfile.write(b"data: [DONE]\n\n")
                return
            return self._send_json(200, {
                "id": completion_id,
                "object": "chat.completion",
                "created": created,
                "model": MODEL,
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": answer},
                    "finish_reason": "stop",
                }],
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            })
        except Exception as exc:
            return self._send_json(500, {"error": {"message": str(exc), "type": "bridge_error"}})


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("opencode Hermes bridge listening on http://127.0.0.1:8765/v1", flush=True)
    server.serve_forever()
