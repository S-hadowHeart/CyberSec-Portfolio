# Large Scope

## What is a large scope anyway ?
- Any program with multiple diffrent websites, commonly:
  - Any subdomain of *.target.domain
  - Any asset that is owned by target
  - Acquisitions of the target
  - Multiple products by the target
- Great places to get started,since you can find unique scope
  - Downside: you need to find the scope yourself
- i've seen companies get report for something they didn't even know was theirs!

- Overwhelmed?
  - Large scope targets can be very overwhelming to new hackers
  - start at everything and make your way down to each application
  - understand the boundaries of each - e.g. Atlassian - JIRA Ticketing

- __Recon__
- For large scope targets recon is key
- just in time Recon
  - single scan on a single day - gives you the lay of the land
  - A lot of new hackers do this
- Passive / Alert recon
  - Looks for new stuff and lets you know when it finds it
  - A lot of the best hackers do this
 
- __Digging for bugs__
- subdomains/domains
  - __Tools__
    - Amass (visual)
    - Sublist3r
  - __What are we trying to do ?__
    - Find domains we can attack
    - you won't just find a bug with recon(usually)
    - You need to ack what you find eventually
    - It can be hard to identify which domains you need to look in more depth
  - __Understanding the data__
  - The Bad News ...
    - Your data usually must be formatted in specific ways for these tools
    - They can be very noisy - and potentially lead to IP bans
    - Screenshots may not be helpful-especially as these tend to work with HTTP only
    - Takes time to go through the data
    - Could find nothing
  - __OSINT__ (open source intelligence)
    - we don't really use  in bug bounty
    - it's depend, how you use
  - __Leaked Keys__ :
    - TruffleHog L to find api etc but many ppl do so may not work
- Code/Version control
- Applications
- Third party services
- API keys/Data Dumps
- Documents
- API Endpoints
- Scope pages
- Tech stack
- Company News

- __Don't overcomplicate things!__
  - You probably don't need a fully custom pipeline at the start
  - you're looking for somewhere to start hacking
  - Easy to invest in infrastructure around recon without

### some Tools:
- __Wappalyzer Tools__
  - Tell what technology use here ...
- __CVEs__
  - __SHODAN tool__
- __Googledorking__
- __News and Updates__

## Remember:
- We're not trying to find bugs at this point
- We're trying to find 'stuff'
  - Might be useful might be useless
- Recon is about more than just a single scan- you need to do it over time
- You'll need to invest into pipelines/notes to get the most out of your recon data

## You have some targets what next?
- Acutually,hacking them
- No different to the main app methodology- treat each like a main app
