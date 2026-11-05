# Contributing

Thanks for wanting to add something. Keep it fun, keep it working.

## What gets in

- It is **free to try**. No key at all is best. A free key is fine, it goes in the 🗝️ column or in Worth the signup.
- It works **today**. Include a **poke it** link that returns a real response in a browser.
- It is **HTTPS**.
- It is **useful or delightful**. Ideally both.

## What does not get in

- APIs that need a credit card before the first request
- Anything built around piracy, scraping personal data, or adult content
- Your company's paid product dressed up as a free API

## How to add one

1. Find the right section. If nothing fits, add it to the closest one and say so in the PR.
2. Add one row in this shape:

   ```markdown
   | [Name](https://docs-url) | One short line about what you get | 🆓 | [poke it](https://example-endpoint) |
   ```

3. Run `python ping.py` and make sure your link comes back 200.
4. Open the pull request with a sentence on why it is cool.

## Removing dead APIs

If `ping.py` shows something has been down for a while, open a PR that removes the row and links to any shutdown notice you found.
