# Using CrewAI for Financial Analysis - AI Makerspace!

<p align="center">
  <img src="https://images.lumacdn.com/cdn-cgi/image/format=auto,fit=cover,dpr=1,quality=75,width=400,height=400/event-covers/a7/d8a6b732-c1e5-4c19-bc4d-409d72aa20d6" />
</p>

---

## Introduction:

In this repository we have built a multi-agent "crew" (powered by [CrewAI](https://github.com/joaomdmoura/crewAI/tree/main)) meant to generate AI-powered financial advisement reports. 

> NOTE: This example does not provide real financial advice, and should not be used to guide investment strategy

## Running the Crew!

We'll explore how to run the crew in detail below!

### Step 1: Cloning this Repository!

1. We'll want to start by cloning this repository, which can be done as follows:

```bash
git clone https://github.com/AI-Maker-Space/AIMS-CrewAI-Demo.git
```

2. Next, we'll `cd` into the newly cloned repository:

```bash
cd AIMS-CrewAI-Demo
```

### Step 2: Initializing Our Environment Variables

We'll be using the following APIs to help us today:

1. [OpenAI's Text Embedding 3 Small Embedding Model](https://platform.openai.com/docs/quickstart)
2. [Anthropic's Claude Sonnet 3.5](https://docs.anthropic.com/en/docs/quickstart)
3. [Sec API](https://sec-api.io/)
4. [SerpAPI](https://serpapi.com/)

Once we've collected all our API keys, we can continue to add them to our `.env` file.

1. Next we'll create a new empty `.env` file to store our actual environment variables in.

```bash 
cp .env.sample .env
```

2. We'll add the content and fill in our API keys in the newly created `.env` file.

### Step 3: Install Dependencies through Poetry

We can install our dependencies straightforwardly using Poetry!

```bash
poetry install --no-root
```

### Step 4: Run the Agent Crew!

All that's left to do now is run the crew, which we can do with:

```bash
python main.py
```

After which it will ask for a company and we're off!

## Credits:

This repository is largely based on the example from the CrewAI creator [@joaomdmoura](https://x.com/joaomdmoura) and the original can be found [here!](https://github.com/joaomdmoura/crewAI-examples/tree/de183dcab06b8021dd403ec4d07116e4ed9b5da8/stock_analysis)
