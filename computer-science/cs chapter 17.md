# Chapter 17: Communication and Internet Technologies — Complete Study Guide
### Cambridge International AS & A Level Computer Science

This is a theory-heavy chapter, so this guide is built the way you actually need to hold it in your head for the exam: every concept explained fully with the reasoning behind it, not just the definition, plus the exact vocabulary the mark scheme rewards, followed by a full worked answer bank for every exam-style question this chapter produces.

---

## PART 1 — TRANSMISSION MODES (17.01)

### 1.1 The big picture question this section answers

When two computers need to talk to each other across a network, there are exactly two fundamentally different ways to organise that conversation: **circuit switching** and **packet switching**. Everything else in this section is detail underneath that one choice.

### 1.2 Circuit switching

**What it is:** a dedicated, continuous physical/logical path (a "circuit") is set up between sender and receiver **before** any data moves, and that path stays reserved for the entire conversation until it's explicitly torn down.

**Where it comes from:** this is the method the traditional telephone system (PSTN — Public Switched Telephone Network) has always used. Even though PSTNs have now largely gone digital, the same switching concept is reused for data transfer — most typically in a **leased line** service, where a business pays for a permanent dedicated circuit.

**The five-step process you must be able to state in order (this is a direct mark-scheme list):**

1. The sender provides the identity of the intended receiver.
2. The system checks whether the receiver is ready to accept data.
3. If the receiver is available, a sequence of links is established across the network (end-systems → local exchanges → intermediate nodes, all with switching functionality).
4. The data is transferred.
5. The links are removed.

**Why this matters — the defining property:** the links between nodes are **dedicated channels in shared transmission media that guarantee unimpeded transmission**. Nobody else's data competes for that channel while it's reserved for you. A phone call has a definite end where the links are torn down; a leased line, by contrast, might stay permanently established.

**Trade-off to understand, not just memorise:** guaranteed bandwidth and consistent latency (good for real-time voice) at the cost of wasted capacity — if you're not actively sending data, the reserved circuit sits idle and unusable by anyone else.

### 1.3 Packet switching

**What it is:** data transmission **without** any dedicated circuit being established first. Data can't be sent as one continuous stream — it's broken up into discrete **packets**, each one able to take a potentially different route across the network.

**Structure of a packet:** a **header** (containing delivery instructions) plus the **data body** (the actual payload). Analogy given in the textbook: like the postal service, but more complex — think of each packet as a separate letter with its own address label, which can travel via different postal routes and arrive out of order.

**Key structural difference from circuit switching:** the links used are **not defined in advance** — a router (acting as a node) decides, packet by packet, where to send things next, rather than a fixed path being reserved beforehand. Nodes in a packet-switched network need more sophisticated functionality than nodes in a circuit-switched one (this extended functionality is what a **router** provides — covered in 17.04).

### 1.4 Connectionless vs connection-oriented service — the two flavours of packet switching

This distinction is asked about constantly and is easy to mix up, so hold onto the mechanism, not just the label.

**Connectionless service:**
- A packet is dispatched with **no knowledge of whether the receiver is ready** to accept it.
- The sender has **no way of finding out whether the transmission succeeded**.
- Fire-and-forget. No acknowledgement expected or checked.

**Connection-oriented service:**
- The **first packet sent includes a request for acknowledgement**.
- If the acknowledgement is received, the sender transmits the remaining packets.
- If no acknowledgement is received, the sender **tries again with the first packet** (retransmission).
- This builds in reliability checking at the transmission level.

**How to remember which is which:** connection-oriented = "let's confirm you're there before I commit to sending everything" (like TCP, later). Connectionless = "here it is, hope it arrives" (like IP, later, or UDP).

---

## PART 2 — PROTOCOLS (17.02)

### 2.1 The definition (exact exam wording — memorise this)

> **Protocol:** a set of rules for data transmission which are agreed by sender and receiver.

That's the whole definition. Deceptively simple, but the exam wants this exact phrasing or something functionally identical to it — "a set of rules" alone is not enough; you need "agreed by sender and receiver" to get full marks, because a protocol is only useful if **both ends** commit to following it.

### 2.2 What kinds of things do the "rules" actually cover?

The textbook gives concrete examples so you can answer "give an example of what a protocol might define" questions:

- **Signal-level rules:** e.g. a protocol could define that a positive voltage represents a bit with value 1.
- **Speed rules:** a protocol might define a maximum transmission speed the sender must not exceed.
- **Format rules:** many protocol rules relate to the **format of a message or part of a message** — e.g. a definition of exactly what the first 40 bytes of a packet must contain.

### 2.3 "A protocol" vs "a protocol suite" — a subtlety worth knowing

When people casually say "a protocol," they often actually mean a **protocol suite** — a bundle containing more than one individual protocol working together (TCP/IP is the classic example: it's a *suite* containing TCP, IP, and many others). Complications layered on top of this:

- There can be **multiple different versions** of the same protocol (e.g. different HTTP versions).
- Protocols often **complement each other** rather than working alone (e.g. TCP complements IP).

---

## PART 3 — THE PROTOCOL STACK (17.03)

### 3.1 Why "stack" as a model at all

Because a protocol suite contains many protocols, and because networking tasks naturally break down into distinct sub-problems (physical signal transmission is a completely different problem from, say, formatting an HTTP request), the suite is organised into **layers**, stacked on top of each other. Each layer solves one specific part of the overall communication problem and hands off to the layer below or above it.

### 3.2 The seven rules of how layers behave — this is a direct list the exam draws from

Learn each one, and more importantly, understand *why* it's true:

1. **Each layer can only accept input from the next higher layer or the next lower layer.** — No skipping layers; a layer never talks directly to a layer two levels away.
2. **There is a defined interface between adjacent layers which constitutes the only interaction allowed between layers.** — The boundary between two layers is a strict contract; each layer only needs to know how to talk to its immediate neighbours, not the internal workings of any other layer.
3. **A layer is serviced by the actions of lower layers.** — Each layer relies on everything below it having already done its job (e.g. the transport layer relies on the network layer to route the packet correctly).
4. **With the possible exception of the lowest layer, the functioning of a layer is created by installed software.** — Only the very bottom layer necessarily touches physical hardware directly; everything above that is implemented in software.
5. **A layer may comprise sub-layers.** — A layer isn't necessarily atomic; it can be internally subdivided (see Ethernet's data-link and physical layers in Part 5, each split into two sub-layers).
6. **Any user interaction takes place using protocols associated with the highest-level layer in the stack.** — The user (or the application they're running) only ever directly deals with the topmost layer (e.g. HTTP at the application layer); everything below is invisible to them.
7. **Any direct access to hardware is confined to the lowest layer in the stack.** — Only the bottom layer physically touches the transmission medium (cables, radio signals, etc).

**Why this design is good — the concept underneath all seven rules:** this is **separation of concerns**. Each layer is an independent, replaceable module. You can swap out the physical medium (e.g. move from cable to Wi-Fi) without changing anything about how HTTP works, because HTTP lives many layers above and only ever talks to its immediate neighbour layer through a defined interface.

---

## PART 4 — THE TCP/IP PROTOCOL SUITE (17.04)

### 4.1 The five-layer network model

```
Application   ← HTTP, SMTP, DNS, FTP, POP3, IMAP
Transport     ← TCP, UDP, SCTP
Network       ← IP, IGMP, ICMP, ARP
Data link
Physical
```

**Critical fact to remember:** TCP/IP as a suite only occupies the **top three layers** (Application, Transport, Network) of this five-layer model. The bottom two layers (Data link, Physical) are supported by a *different* protocol suite entirely — most commonly Ethernet (covered in Part 5). TCP/IP doesn't care how those bottom two layers are implemented, as long as they do their job.

**Naming trap to watch for (explicitly flagged in the textbook as a "tip"):** the "Network" layer is sometimes called the **Internet layer**, and the "Data link" layer is sometimes called the **Link layer**, depending on the source. Don't be thrown by this in an exam question that uses different terminology than you're used to — they're the same layers.

### 4.2 The logical peer-to-peer relationship — the conceptual trick that makes layering work

Here's the mental model: an application running on one end-system behaves **as though** it has a direct connection to an application on a different end-system — even though in reality the data physically travels down through all the layers on the sender's system, across the network (possibly through router(s), which only process up to the network layer), and back up through all the layers on the receiver's system.

The flow in words:
1. The application layer protocol on the sender sends a "message" down to the transport layer protocol **on the same system**.
2. The transport layer initiates a process that results in the **identical message** eventually being delivered to the transport layer **on the receiver end-system**.
3. On the receiver end-system, the transport layer's final job is handing that identical message up to the application layer protocol.

Each layer only "talks" logically to its **corresponding layer** on the other end-system (this is the "logical peer-to-peer relationship" shown by the horizontal dashed lines in Figure 17.02) — even though physically the data is going down and across and up, not straight across.

**A router's role in this diagram:** a router only has a protocol stack that goes up to the **network layer** — it doesn't run application or transport layer protocols. This is exactly why a router can forward packets between networks without needing to understand what application generated them.

### 4.3 TCP (Transmission Control Protocol) — full mechanism

TCP operates at the **transport layer**. Its job: take the user data handed down from the application layer and guarantee its **safe delivery** to the receiver.

**What TCP does, step by step:**
1. TCP creates **sufficient packets** to hold all of the data being sent.
2. Each packet = a **header** + the **user data**.
3. The header includes the **port number** identifying the application-layer protocol at the sender's end (e.g. **port 80 for HTTP** — memorise this specific number, it's commonly tested).
4. The header also includes the **port number of the receiving end-system's application layer protocol** — so the response can be routed back to the correct application.
5. **Critically: TCP is NOT concerned with the address of the receiving end-system.** That's IP's job, not TCP's. This separation of responsibility is a favourite exam distinction.
6. If a packet is part of a sequence, TCP includes a **sequence number**, so the receiver can reassemble the data in the correct order even if packets arrive out of order.

**TCP is connection-oriented** (ties back to 1.4): following the connection-oriented procedure, TCP initially sends just **one packet** of the sequence to the network layer. Only once the network layer confirms back to the transport layer that the connection has been established does TCP send the rest of the packets — and it continues to receive acknowledgement packets in response, which lets it detect and re-send any missing packets.

### 4.4 IP (Internet Protocol) — full mechanism

IP operates at the **network layer**. Its job: ensure **correct routing** over the Internet.

**What IP does, step by step:**
1. IP takes the packet handed down from the transport layer (from TCP).
2. It adds **its own header** on top, containing the **IP address of the sender** and the **IP address of the receiver**.
3. To find the receiver's IP address, IP is very likely to use the **DNS (Domain Name System)** service to resolve the URL supplied in the user data into an actual IP address.
4. The resulting packet — now called a **datagram** — is sent down to the **data-link layer**, which is a different protocol suite (Ethernet).
5. **Once the datagram is handed to the data-link layer, IP's job is completely finished.** It has no further duty for that packet.

**IP is a connectionless service** (again, ties back to 1.4): once a packet is sent, IP has **no knowledge whatsoever of whether it reached its destination**. If IP later receives a packet containing an acknowledgement for something previously sent, it simply passes that acknowledgement straight up to TCP without inspecting or understanding its content — IP doesn't process acknowledgements, it just relays them.

**The clean division of labour to hold onto for exam questions comparing TCP and IP:**

| | TCP | IP |
|---|---|---|
| Layer | Transport | Network |
| Responsible for | Safe, ordered, complete delivery of data | Correct routing/addressing across the Internet |
| Concerned with addresses? | No — only port numbers | Yes — sender and receiver IP addresses |
| Connection type | Connection-oriented | Connectionless |
| Uses acknowledgements? | Yes, actively manages them | No, just passes them through to TCP |

### 4.5 The router — how it actually works as a node

When a frame (built by the data-link layer) arrives at a router during transmission, the **datagram content is handed back up to IP** at that router. It's now the **router's software's job** to decide the next target host in the transmission chain.

**How the decision is made:** the router software consults a **routing table** specific to that router.

**Important scale fact:** the Internet is far too large and complex for any single router to hold a **global** routing table (i.e. no router knows the full map of the entire Internet) — each router's table is necessarily local/partial.

**What routing tables also track:** details of any **current problems** with the available options for the next transmission step, which lets the routing decision account for congestion or failures and deliver packets in the **shortest possible time available**.

**Router vs switch — a commonly tested distinction:**

| | Router | Switch |
|---|---|---|
| Layer it operates at | Up to the network layer | Only the data-link layer |
| Makes routing decisions? | **Yes** | **No** — a frame arriving at a switch is simply passed on without any routing decision |
| Access to network layer? | Yes | **No** |

---

## PART 5 — THE ETHERNET PROTOCOL STACK (17.05)

### 5.1 Why Ethernet exists alongside TCP/IP

Ethernet is a protocol suite designed for a **local area network (LAN)**. It can function entirely in isolation, with no connection to the Internet at all. But in practice, almost every LAN today is connected to the Internet — so a LAN's Ethernet protocol suite needs to **support** the TCP/IP suite running above it.

**How the layers fit together:** TCP/IP occupies the top three layers of the five-layer stack (Application, Transport, Network) and is **supported by** the bottom two layers (Data link, Physical) — and Ethernet is the most likely protocol suite to be providing exactly those bottom two layers. TCP/IP itself doesn't care *how* those two layers are implemented, only that they work.

**A modelling nuance to be aware of:** some sources use only a **four-layer stack** for an end-system instead of five. This happens for one of two reasons: either the model only includes layers handled entirely by software (dropping the strictly-hardware bottom layer from the count), or the model amalgamates all of TCP/IP's supporting functionality into a single combined layer. Don't be confused if a diagram you see elsewhere has four layers instead of five — it's a modelling choice, not a contradiction.

### 5.2 The four Ethernet sub-layers

Ethernet is best understood as **two logical sub-layers within each of the Data link and Physical layers**:

```
Data link layer:
    LLC  (Logical Link Control)
    MAC  (Medium Access Control)

Physical layer:
    PCS  (Physical Coding Sublayer)
    PMA  (Physical Medium Attachment)
```

**LLC (Logical Link Control):**
- Responsible for the **interaction with the Network layer** above it.
- Manages data transmissions and ensures the **integrity** of those transmissions.
- **Because Ethernet is a connectionless protocol**, LLC has **no responsibility for checking that a transmission was successfully delivered** — this parallels IP's connectionless behaviour at the layer above.

**MAC (Medium Access Control):**
- Responsible for **assembling the Ethernet packet**, which at this layer is called a **frame**.
- Two key components it adds: the **address of the transmitter** and the **address of the receiver**.
- Also **initiates frame transmission** and **handles recovery from transmission failure due to a collision** — commonly using **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection).

**PCS (Physical Coding Sublayer):**
- Responsible for **coding data ready for transmission**, or **decoding data received**.
- It either receives a frame from MAC (to encode and send) or sends a frame up to MAC (after decoding something received).

**PMA (Physical Medium Attachment):**
- Responsible for the actual **signal transmitting and receiving** — the lowest-level, closest-to-the-wire job.

**A useful way to remember the flow:** LLC talks to the layer above (Network); MAC builds the actual frame with addresses and handles collisions; PCS converts between frame-data and physical signals; PMA is the literal electrical/optical/radio transmission. Data flows down through this list to send, and up through it (in reverse) to receive.

### 5.3 MAC addresses

**Definition:** both addresses assembled into an Ethernet frame by MAC (transmitter and receiver) are examples of **physical addresses**, more commonly called **MAC addresses**. A MAC address **uniquely identifies one NIC** (Network Interface Card).

**Technical detail worth knowing:**
- Standard MAC addresses are **48 bits** long. This has so far been sufficient to guarantee every NIC in existence gets a unique address.
- There is a **64-bit alternative**, already used occasionally, reserved for future use once 48 bits eventually proves insufficient.
- The 48-bit address is conventionally written in **hexadecimal notation**, e.g.: `4A:30:12:24:1A:10`
- In one common addressing scheme, **the first three bytes identify the manufacturer** of the NIC.

**Why this matters conceptually:** a MAC address is a *physical/hardware* identity tied to a specific network card, completely separate from an IP address, which is a *logical* address assigned by the network and can change depending on which network you connect to. This IP-vs-MAC distinction is a classic point of confusion the exam likes to probe.

---

## PART 6 — APPLICATION-LAYER PROTOCOLS (17.06)

### 6.1 HTTP (HyperText Transfer Protocol)

**The single most important application-layer protocol**, because it underpins the entire World Wide Web. Every time you access a website through a browser, HTTP is running, invisibly, underneath.

**Common exam trap explicitly flagged in the textbook:** do not confuse **HTTP** with **HTML**. HTTP is the *protocol* used to transfer web content; HTML is the *markup language* used to structure the content of a web page. They are completely different things at completely different levels.

**Nature of HTTP:**
- **Transaction-oriented**, **client–server** protocol.
- A transaction = the client sends a **"request"** message, and the server sends back a **"response"** message.

**Format of an HTTP request:**
- The first line of a request message is the **request line**.
- Optionally followed by **header lines**.
- All of this is encoded using **ASCII**.
- The format of the request line is:

  ```
  <Method> <URL> <Version>CRLF
  ```

  where **CR** and **LF** are the ASCII carriage return and line feed characters (marking the end of the line).

- The **method** in the request line is usually **GET**, but there are several alternative methods available, which is exactly why HTTP is applicable to more than just fetching web pages — it's a general-purpose request/response protocol.
- The **version** must be specified because HTTP has evolved over time, so more than one version exists in active use simultaneously.

### 6.2 Email protocols — the three-hop journey

**The setup (Figure 17.04):** sending an email from sender to receiver is **not one connection** — it's **three separate, individual client–server interactions** chained together:

```
Email sender client  --SMTP-->  Sender's mail server  --SMTP-->  Receiver's mail server  --POP3-->  Email receiver client
```

Notice the role-switching: the sender's mail server first acts as a **server** (receiving from the sending client), then immediately has to act as a **client** itself when it forwards the message onward to the receiver's mail server.

**SMTP (Simple Mail Transfer Protocol):**
- A **"push"** protocol — the sender actively pushes the message toward its destination.
- Used for: client → sender's mail server, and mail server → mail server.

**POP3 (Post Office Protocol version 3):**
- A **"pull"** protocol — the client pulls (downloads) mail off the server.
- Emails are **downloaded onto the client computer**.
- Once downloaded, emails are **only accessible from that one client system**.

**IMAP (Internet Message Access Protocol) — the more recent alternative to POP3:**
- Emails are **not downloaded**; they **remain stored on the server** but stay accessible from the client.
- The client effectively views/manages mail that lives permanently on the server.

**The security/accessibility trade-off between POP3 and IMAP (a favourite exam comparison):**

| | POP3 | IMAP |
|---|---|---|
| Where email lives | Downloaded to local client | Remains on the server |
| Accessible from multiple devices? | **No** — only from the one client it was downloaded to | **Yes** — accessible from any client, ideal for someone on the move or using a different system |
| Security argument | Can be argued **more secure against cyber-attack** because emails are stored locally, off the server | Depends on server security, but the server is typically **backed up regularly**, whereas a local client "might not be" |

**A historical/practical note the textbook makes:** SMTP has largely been **replaced by web-based mail** — when you use a browser to access your email application, **HTTP** is now the protocol actually being used for that client-facing interaction. However, **SMTP remains in active use for transfers between mail servers** (the middle hop in the three-hop chain above never went away).

### 6.3 FTP (File Transfer Protocol)

**Why it's needed:** the most common way to send a file between two people is to attach it to an email — but this isn't always a suitable method (e.g. very large files, or automated/bulk transfers). FTP is the **application-layer protocol built specifically to handle file transfer** between any two end-systems.

**The core technical challenge FTP solves:** file transfer isn't simple when the two end-systems run **different operating systems with different file systems**. FTP handles this by **separating the control process from the data-transfer process** — i.e. the connection used to issue commands (like "list files," "change directory") is kept separate from the connection actually used to move the file bytes.

**Practical use case flagged in the textbook:** if you were setting up a website, you'd need to **upload files to a server** — this is a classic real-world use of FTP.

---

## PART 7 — PEER-TO-PEER (P2P) FILE SHARING (17.07)

### 7.1 What P2P architecture actually is

P2P generates a huge fraction of all Internet traffic. Its defining structural feature: **no structure and no controlling mechanism** — there's no central server orchestrating everything.

**Key vocabulary:**
- **Peer:** an end-system that acts as **both client and server simultaneously**.
- **Seed:** a peer, specifically when it is acting **as a server** (i.e. uploading/providing content to others).

### 7.2 BitTorrent — the dominant P2P protocol

BitTorrent is the most-used P2P protocol because it enables **fast sharing of files**. The textbook frames BitTorrent around **three basic problems** it has to solve — this three-part structure is exactly how exam questions probe this topic, so learn it as three distinct problems with three distinct solutions.

**Problem 1: How does a peer find others that have the wanted content?**

- Solution: every content provider supplies a **torrent** file — a small content-description file.
- The torrent file contains: the **name of the tracker** (a server that leads peers to the content) and a **list of the chunks** that make up the full content.
- Size fact worth remembering: the torrent file is **at least three orders of magnitude smaller** than the actual content, so it can be transferred and shared very quickly.
- The **tracker** is a server that maintains a list of **all the other peers** actively downloading and uploading that content — this collective group of active peers is called the **swarm**.

**Problem 2: How do peers replicate content to provide high-speed downloads for everyone?**

- Solution: peers **download and upload chunks simultaneously** (not sequentially — this is what makes BitTorrent fast, since every downloading peer is also immediately helping upload to others).
- Peers exchange lists of which chunks they have, and specifically **aim to download the rarest chunks first** — this is a deliberate strategy.
- The self-correcting mechanic: the moment a rare chunk gets downloaded by another peer, **it automatically becomes less rare**, since now more peers hold it and can redistribute it. This spreads the content's availability evenly and quickly across the whole swarm.

**Problem 3: How do peers encourage other peers to actually contribute content, rather than just leeching?**

- The problem being solved: **free-riders** (also called **"leechers"**) who only download and never upload.
- The solution: a peer initially tries other peers **at random**, but then **only continues to upload** to peers that are themselves **providing regular downloads** back in return — a reciprocity mechanism.
- If a peer isn't uploading, or is only uploading slowly, that peer is eventually **isolated**, or **"choked"** — cut off from receiving further content from others.

**A note the textbook explicitly makes:** BitTorrent's terminology is unusual, and there are other specialised terms in use beyond the ones covered here — but the underlying *principles* (find peers via a tracker, prioritize rare chunks, punish free-riders) are straightforward once you separate them into these three problems.

---

## PART 8 — CHAPTER SUMMARY (the exact revision bullet points)

- Circuit switching requires a dedicated circuit to be established between sender and receiver before transmission can start.
- In packet switching, packets can be transmitted without any circuit being created.
- Packet switching can use connectionless or connection-oriented transmission.
- A protocol suite is implemented as a layered stack.
- The TCP/IP protocol suite supports usage of the Internet.
- Ethernet is the most likely option for use in the Network and Data link layers.
- Examples of application-layer protocols are HTTP, SMTP, POP3, IMAP and FTP.
- Peer-to-peer file sharing on the Internet uses the BitTorrent protocol.

---

## PART 9 — FULL WORKED EXAM-STYLE ANSWERS

### Question 1 — Locating data within an IP datagram structure

Structure given: `IP Header | TCP Header | TCP Content`

| Item | Location | Why |
|---|---|---|
| a. Destination address | **IP** | IP is responsible for addressing (sender/receiver IP addresses); TCP is not concerned with end-system addresses at all |
| b. Sender address | **IP** | Same reasoning — addressing lives in the IP header |
| c. Destination port | **TCP** | Port numbers identify application-layer protocols and are TCP's responsibility, not IP's |
| d. Sender port | **TCP** | Same reasoning |
| e. Packet sequence number | **TCP** | TCP includes sequence numbers to allow correct reassembly of packets that may arrive out of order |
| f. Acknowledgement | **TCP** | Acknowledgements are part of TCP's connection-oriented mechanism; IP passes acknowledgement packets straight through to TCP without processing them |

### Question 2 — Ethernet + TCP/IP combined

**(a) Diagram [5 marks]** — should show the five-layer stack with TCP/IP clearly occupying the top three and Ethernet's sub-layers supporting the bottom two:

```
Application  ─────────────┐
Transport     ─── TCP/IP ──┤
Network      ─────────────┘
Data link    ── LLC / MAC ──┐
Physical     ── PCS / PMA ──┘── Ethernet
```

Marks awarded for: correct five layers named in order, TCP/IP correctly bracketed to top three layers, Ethernet correctly bracketed to bottom two with its four named sub-layers (LLC, MAC, PCS, PMA) shown.

**(b) Explain "MAC address" [3 marks]**

A MAC address is a **physical address** that **uniquely identifies one NIC** (network interface card) [1]. It is **48 bits** long, conventionally written in **hexadecimal notation** [1]. It's assigned to the network hardware itself, unlike an IP address which is a logical address assigned by the network the device connects to [1].

### Question 3 — Methods for one end-system to get a copy of a file from another

**(a) Three possible methods [6 marks — 2 each]**

1. **Email attachment** — the file is attached to an email message and sent from the sender's client to the receiver's client via mail servers.
2. **Direct file transfer via FTP** — the file is uploaded/downloaded between the two end-systems using a dedicated file-transfer connection, handling differences in operating system/file system between the two ends.
3. **Peer-to-peer sharing (BitTorrent)** — the file is broken into chunks and distributed via a swarm of peers, coordinated by a tracker, rather than transferred directly between the original two systems.

**(b) Application-layer protocols used by each method [8 marks]**

1. Email attachment → **SMTP** (push, client to server, and server to server) and **POP3 or IMAP** (pull, server to receiving client).
2. Direct file transfer → **FTP**, which separates the control connection from the data-transfer connection to cope with differing file systems.
3. P2P sharing → **BitTorrent**, using a torrent file and tracker server to coordinate chunk exchange across a swarm of peers.

### Question 4 — Email protocols explained [12 marks]

**SMTP:** used to **push** an email from the sender's client to their outgoing mail server, and then from that mail server onward to the recipient's mail server. It is not typically used for the final "download" step to the receiving client anymore.

**POP3:** used by the receiving client to **pull/download** the email from the receiver's mail server onto the local client device. Once downloaded, the email is only accessible from that one device; it can be argued this is more secure against cyber-attack since it isn't sitting on a remotely-accessible server.

**IMAP:** an alternative to POP3 where the email is **not downloaded** — it stays stored on the server and is accessed remotely from whichever client the user is using. This makes it ideal for users who move between devices or locations, at the cost of depending on the server (rather than local storage) for security and availability, though servers are typically backed up regularly.

**HTTP:** with the rise of **web-based mail**, users now access their email application through a **browser**, meaning HTTP is the protocol actually carrying that client-facing interaction — SMTP has been largely displaced for this particular leg, although it remains in use for server-to-server transfer.

*(Diagram suggestion for full marks: reproduce the three-hop chain — client –SMTP→ mail server –SMTP→ mail server –POP3/IMAP→ client — and annotate each hop with the protocol used.)*

### Question 5 — Cambridge 9608 Paper 31, June 2015, Q6

**(a) Matching descriptions to protocols [4 marks]**

| Description | Protocol |
|---|---|
| Email client downloads an email from an email server | **POP3** |
| Email is transferred from one email server to another email server | **SMTP** |
| Email client sends email to email server | **SMTP** |
| Browser sends a request for a web page to a web server | **HTTP** |

**(b) Name the model used for direct download (as opposed to BitTorrent) [1 mark]**

**Client–server model.**

**(c) BitTorrent function explanations**

**i. Tracker [2 marks]** — a server that maintains a list of all the other peers (the swarm) that are actively downloading and uploading a particular piece of content; it helps a new peer find others who have the content it wants.

**ii. Seed [2 marks]** — a peer that is acting **as a server**, i.e. it holds content and is uploading/providing it to other peers in the swarm.

**iii. Swarm [2 marks]** — the collective group of all peers that are currently actively downloading and uploading a specific piece of content, coordinated via the tracker.

### Question 6 — Cambridge 9608 Paper 31, November 2015, Q3

**(a) Two items in an email packet apart from the data [2 marks]**

Any two of: a **header**; **sender/receiver address information**; a **sequence number** (if part of a multi-packet sequence); **port number** information.

**(b) Role of routers in sending the email between mail servers [3 marks]**

Each router receives the frame from the data-link layer and passes the datagram content back up to IP [1]. The router's software then consults its **routing table** to decide the next target host/hop for the datagram [1]. Since no single router holds a global routing table of the entire Internet, this decision-making is repeated hop-by-hop across multiple routers until the datagram reaches its destination network [1].

**(c) Why packet switching is appropriate for sending an email [2 marks]**

Email is not a real-time, continuous stream of data that needs a permanently reserved circuit [1]; it can tolerate the data being broken into packets, transmitted independently (potentially via different routes), and reassembled at the destination without the user noticing any delay-sensitivity issues, so the flexibility and efficient shared use of network capacity that packet switching offers is well suited to it [1].

**(d) Name an alternative communication method [1 mark]**

**Circuit switching.**

**(e) An application for which circuit switching is appropriate, with justification [3 marks]**

**Real-time voice/telephone calls** [1]. Justification: voice communication is highly sensitive to delay and requires a consistent, guaranteed, unimpeded channel for the duration of the call [1] — packet switching's variable routing and potential for delay/reordering would cause unacceptable disruption to a live conversation, whereas a dedicated circuit guarantees the necessary continuous, low-latency channel [1].

---

## PART 10 — QUICK-FIRE DEFINITION DRILL

Practise stating each of these from memory, in the exact style the exam rewards:

1. **Protocol** — a set of rules for data transmission which are agreed by sender and receiver.
2. **Circuit switching** — a dedicated circuit is established between sender and receiver before transmission starts, and removed afterwards.
3. **Packet switching** — data is broken into packets, each with a header and data body, and transmitted without a pre-established circuit.
4. **Connectionless service** — a packet is sent with no way of knowing whether the receiver is ready, or whether the transmission succeeded.
5. **Connection-oriented service** — the first packet requests acknowledgement; further packets are only sent once that acknowledgement is received, with retransmission if it isn't.
6. **MAC address** — a physical address that uniquely identifies one NIC, typically 48 bits, written in hexadecimal.
7. **Datagram** — the name given to an IP packet once IP has added its header (sender/receiver IP addresses) and passed it to the data-link layer.
8. **Frame** — the name given to the packet once the data-link layer (via MAC) has assembled it, adding transmitter/receiver MAC addresses.
9. **Tracker** — a server maintaining a list of peers (the swarm) currently sharing a particular piece of content in BitTorrent.
10. **Seed** — a peer acting as a server (i.e. uploading) in a P2P network.
11. **Leecher** — a peer that only downloads and doesn't contribute uploads back to the swarm.

---

## PART 11 — SELF-TEST CHECKLIST

- [ ] State the five-step process of circuit switching, in order.
- [ ] Explain the difference between connectionless and connection-oriented service, with an example protocol for each (IP / TCP).
- [ ] List all seven rules of how protocol stack layers behave.
- [ ] Draw the five-layer network model and correctly label which three layers TCP/IP occupies.
- [ ] Explain, precisely, what TCP is responsible for vs what IP is responsible for — especially the "TCP doesn't handle addresses, IP doesn't handle ports" distinction.
- [ ] Explain what a router does with a datagram when a frame arrives, and why no router has a global routing table.
- [ ] State the difference between a router and a switch in terms of which layer each operates at.
- [ ] Name and describe the function of all four Ethernet sub-layers (LLC, MAC, PCS, PMA).
- [ ] Explain what a MAC address is and how it differs conceptually from an IP address.
- [ ] Distinguish HTTP from HTML clearly (common trap).
- [ ] Write out the format of an HTTP request line, including what CRLF stands for.
- [ ] Trace the full three-hop journey of an email and name the protocol used at each hop.
- [ ] Compare POP3 and IMAP on: where email is stored, multi-device access, and security trade-offs.
- [ ] Explain why FTP separates control from data transfer, and why that's necessary.
- [ ] Explain BitTorrent's three problems and their solutions: finding peers (tracker/torrent/swarm), replicating content fast (rarest-chunk-first), and discouraging free-riders (choking leechers).
- [ ] Justify, for a given real-world scenario, whether circuit switching or packet switching is the more appropriate choice — and why.

---

*This guide is built directly from Cambridge International AS & A Level Computer Science, Chapter 17, incorporating the exact terminology, five-layer model, and worked past-paper questions (9608 Paper 31, June 2015 and November 2015) as printed in the chapter.*