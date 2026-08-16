# Collections Research - Build Pack (for subagent parcel-out)

## Mission
Scrape and extract EVERYTHING from the assigned sources, down to full verbatim essay text,
dialogue, and quoted AO/expert commentary - then write one research file with max density.
Sweep the Live Wire links in parallel with web_search_plus for "near-identical" recent essays.

## Where to write output
Output ONE markdown file per agent at the exact path given in your task. Include a Sources
section with every verified URL. Include excerpt length guidance.

## Working extractor ladder (from lab memory - Web Tools on this box fail keyless on some sites)
1. web_extract_plus(url) - try FIRST (verify the provider fallback auto-mode; the previous agent
   confirmed provider='keenable' works fully keyless)
2. If empty/blocked -> r.jina.ai via terminal: `curl -s "https://r.jina.ai/<URL>"` (works on
   Cloudflare-walled pages; CEG + most blogs). Add header "-H 'X-With-Images-Placeholder: true'"
   and print to a file with >.
3. If still empty -> browser not available to subagents (requires approval). Skip and note it.
Every URL must be verified live (fetch attempt logged), not assumed. If a source 403s, try the
r.jina.ai mirror, then note the blockage and move on.

## Verbatim essay text = the deliverable
For accepted-essay pages that list N essays, extract the FULL TEXT of every essay you can, not a
summary. These are the raw material my user wants. Commentary/AO quotes: keep verbatim too.
For analysis-only pages: keep all direct quotes, drop filler prose.

## Priority ordering within each file
1. Full essay texts (highest)
2. AO / expert / coach commentary verbatim
3. Techniques / patterns / takeaways as bullets with quoted evidence
4. Fully-verified source list at the end

Output language: English. No fabricated quotes - only what you actually extracted. If a source
gives nothing after two extraction attempts, mark it BLOCKED and do not invent content.

## Report back
Your final summary = the file path + file size + count of full essays extracted + count of
verbatim AO/expert quotes + any sources that failed.