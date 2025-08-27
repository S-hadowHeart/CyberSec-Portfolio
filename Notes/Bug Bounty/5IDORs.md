# IDORs 
- Insecure direct object references (IDORs)
## What ?
- Access COntrol
- Allows you to access a resource you don't own , if you know it's identifier
- Can affect any CRUD action (create read update delete)
## Where ? 
- Broad scope applications
- Any client that users IDs, numeric / auto incrementing (1,23...) , alphanumeric  IDs or UUIDs
- Very Common on API (Large attack surface)
- Ecommerce, social media , saas Applications
- Anything with complex permission
## why ?
- Breaks the permission model of an application
- You can view sensitive data OR make unauthorised changes
- Often can be chained into impactful exploits
## How ?
- 2 accounts , your victim and your attacker
- On the victim account use the web app like normal
- Repeat the request or intercept the request and replace the victim's cookies with the attackers
- or use automated tool like __Autorize__ to do it automatically
