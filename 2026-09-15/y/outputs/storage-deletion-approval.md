# Storage deletion approval checklist

Nothing in this checklist has been deleted.

## Requested deletion candidates

| Approve? | Item | Current size | Risk / effect |
|---|---|---:|---|
| ☐ | VS Code WebStorage | 2.5 GiB | Rebuildable web/editor state; may remove extension sign-in/session data. |
| ☐ | VS Code CachedExtensionVSIXs | 703 MiB | Downloaded extension installers; generally safe, extensions remain installed. |
| ☐ | VS Code agent-host | 285 MiB | Agent runtime/cache; may be recreated. |
| ☐ | VS Code application data / anything under `Application Support/Code` | about 3.8 GiB total | Broad deletion can remove settings, extensions, profiles, and workspace state. Review before approving. |
| ☐ | Antigravity IDE WebStorage | 1.0 GiB | Web/session state; may sign you out or remove local web data. |
| ☐ | Antigravity CachedData | 128 MiB | Rebuildable cache. |
| ☐ | Antigravity CachedExtensionVSIXs | 120 MiB | Downloaded extension installers; generally safe. |
| ☐ | Antigravity IDE cache-related data | about 1.1 GiB | Broad deletion may remove local state; review exact subfolders first. |
| ☐ | Whisky Libraries | 854 MiB | Windows game/runtime libraries; deleting may break installed Whisky games. |
| ☐ | Whisky container | 426 MiB | Bottles and app data; deleting removes Windows prefixes/configuration. |
| ☐ | OpenCode cache backup | 641 MiB | Looks like a dated backup; verify it is not needed for recovery. |
| ☐ | Orchids | 484 MiB | App data plus checkpoints/cache; deletion may remove local history/state. |
| ☐ | Orchids checkpoints | 277 MiB | Saved checkpoints; delete only if those recovery points are unwanted. |
| ☐ | Orchids cache | 195 MiB | Likely rebuildable cache. |
| ☐ | Apple wallpaper support data | 457 MiB | Wallpaper assets; macOS may redownload them. |
| ☐ | Apple wallpaper agent container | 562 MiB | Wallpaper service data; may reset wallpaper assets/settings. |
| ☐ | Aside | 416 MiB | App data; may remove local state. |
| ☐ | Aside component cache | 56 MiB | Likely rebuildable browser-component cache. |
| ☐ | Comet | 364 MiB | App data/profile; may sign out or remove local browsing state. |
| ☐ | Comet Default profile | 208 MiB | Profile data; could remove local settings/session data. |
| ☐ | Comet component cache | 50 MiB | Likely rebuildable cache. |
| ☐ | Code/agent-host | 285 MiB | Agent runtime data; likely rebuildable but review first. |
| ☐ | GitKrakenCLI (versions and related data) | 282 MiB | CLI versions; deleting may force a redownload. |
| ☐ | Qoder bin | 88 MiB | Installed helper binary; may be redownloaded. |
| ☐ | Cloud Code | 117 MiB | App support data for Cloud Code; may remove local state. |
| ☐ | iFlyDown | 54 MiB | App support data; effect depends on whether downloads are stored there. |
| ☐ | Codex component cache | 55 MiB | Rebuildable component cache. |
| ☐ | Claude Cache | 91 MiB | Rebuildable cache; may require downloads again. |

## Container candidates

| Approve? | Container | Size | Recommendation |
|---|---|---:|---|
| ☐ | iLovePDF | 247 MiB | Delete only if you do not need its local documents/state. |
| ☐ | Safari | 196 MiB | You said you use Chrome; deleting may remove Safari local data. |
| ☐ | Dynamic Wallpaper | 105 MiB | Likely wallpaper assets; generally nonessential. |
| ☐ | Apple geod | 122 MiB | Location/geodata cache; usually rebuildable, but Apple-managed. |
| ☐ | Siri text-to-speech data | 523 MiB | Voice assets; may trigger redownloads or affect offline voices. |
| ☐ | Media Analysis data | 500 MiB | Photos/media analysis indexes; deleting can trigger re-indexing. |
| ☐ | Avatar Picker / Memoji | 39 MiB | Apple UI assets; small and not worth risking system behavior. |
| ☐ | Docker | 2.6 GiB | Not requested for deletion; may contain images, containers, and volumes. Keep unless explicitly approved. |
| ☐ | WhatsApp | 425 MiB | Personal app data; keep unless explicitly approved. |

## Cache-only candidates to review (not deleted)

| Approve? | Cache | Size | Notes |
|---|---|---:|---|
| ☐ | Google caches | 3.5 GiB | Generally safe; browser may rebuild/download data. |
| ☐ | Spotify cache | 1.3 GiB | Safe-ish; offline/downloaded cache may need rebuilding. |
| ☐ | Codex cache | 722 MiB | Rebuildable. |
| ☐ | Python cache | 417 MiB | Rebuildable package/runtime cache. |
| ☐ | OpenCode updater cache | 286 MiB | Rebuildable updater files. |
| ☐ | Ollama cache | 172 MiB | Could remove cached support files; model data may live elsewhere. |
| ☐ | Electron cache | 109 MiB | Rebuildable. |
| ☐ | GeoServices cache | 82 MiB | Rebuildable location cache. |
| ☐ | Bun cache | 187 MiB | Rebuildable package cache. |
| ☐ | pip cache | 46 MiB | Rebuildable Python package cache. |
| ☐ | Homebrew cache | 54 MiB | Rebuildable downloads. |
| ☐ | Steam cache | 33 MiB | Rebuildable. |

## Applications and explanations

| Application | Size | What it is |
|---|---:|---|
| Microsoft Outlook | 1.6 GiB | Microsoft email/calendar client; deleting its app data can affect local mail cache and settings. |
| Visual Studio Code | 1.4 GiB | Code editor; deleting the app removes the editor, while deleting `Application Support/Code` removes settings/extensions/state. |
| Discord | 479 MiB | Chat/voice application; its support data can include local caches and session state. |
| OpenMausBot | 690 MiB | Kept as requested. |

## Important distinction

“Discord app 0.0.411” is an internal Discord application-version folder under Application Support. It is not a separate Discord installation. The `/Applications/Discord.app` bundle is the main application.

“Steam.AppBundle” is Steam’s application bundle/support package. It is separate from game libraries, but deleting it can make Steam repair or redownload itself.

## Approval format

Reply with the exact rows or paths to approve, for example:

`Delete: VS Code WebStorage, VS Code CachedExtensionVSIXs, Google caches, Safari container`

I will then re-check the exact paths and show the final deletion set before taking action.
