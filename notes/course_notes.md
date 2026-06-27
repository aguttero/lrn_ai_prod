# day 1 - instant.py
## VERCEL SETUP
see zreources/week1/day1.md 
https://vercel.com/docs/getting-started-with-vercel

## Vercel add env API KEY
```bash
vercel env add OPENAI_API_KEY
```
```bash
vercel env add GEMINI_API_KEY
```
### vercel deploy info
cmd + click in terminal or vercel dashboard

## vercel link
```bash
vercel link
```
use this command whebn project already has api/index.py and vercel required files (so no vercel.json is needed)

## vercel deploy
```bash
vercel .
```
### redeploy to preview:
vercel .
### redeply to production
vercel . --prod

## Local Uvicorn test
```bash
cd src
uvicorn inst_loc:app --reload  #inst_loc.py is the python filename
```


# Frontend
## React Libraries
Examples:
Material UI
Chakra

# day 2 - Next app
## setup
0. node.js installed as prerequisite
1. cd to projects folder
2. Create a new 'saas' Next.js project with TypeScript. This command is a bit longer than the one I type in the video, to account for a recent change:  
video command: npx create-next-app saas --ts

```bash
npx create-next-app saas --ts --eslint --tailwind --no-src-dir --no-app
```
questions:
which linter? ESlint
Tailwind CSS? Yes
src dir? No (Yes for larger projects)
app router? no (will use pages router this time)
turbopack? no
custom import alias? no
