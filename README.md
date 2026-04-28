# Singapore Mahjong

A modular Python implementation of Singapore-style Mahjong, featuring a custom game engine, scoring system, and AI agents.

This project focuses on building a clean, extensible architecture for turn-based games, with the long-term goal of developing competitive Mahjong AI, possibly using heuristic and Monte Carlo methods.

---


## Project Goals

- Build a fully functional Mahjong game engine
- Implement Singapore-style scoring rules
- Develop AI agents
- Create a platform for experimentation and improvement of strategies




## Why This Project?

Unlike more commonly implemented variants (e.g. Riichi Mahjong), Singapore Mahjong lacks open-source implementations.
It also allows me to explore game state modelling, combinatorial hand evaluation and AI strategy development
This project is also built alongside CS61A concepts, and serves as a way to practice implementing them, concepts including:

Data abstraction

Object-oriented programming

Recursive problem solving

State management




## Architecture Overview

The project is structured into independent modules:

engine - Core game logic

rules - Win detection and scoring

ai - AI agents (eg: random, heuristic, Monte Carlo)

interface - interface for gameplay

tests - Unit tests




## Current Features (tracking purposes)

- Tile and table representation
- Tile encoding and table set-up
- [WIP] hand representation




## Features to be added
### 1: Core Engine
- Tile, Wall, Hand classes [Done]
- Draw-discard loop [Done]
- Turn-based game loop

### 2: Game Logic
- Valid move detection
- Dealing and playing functions
- Winning hand detection

### 3: Scoring
- Win detection algorithm
- Singapore Mahjong scoring system
- Hand and set calculation

### 4: AI
- Random AI
- Heuristic-based AI
- Hand evaluation
- Monte Carlo simulation
- Hidden Markov Model 

### 5: (Optional)
- Web interface
- Multiplayer support
- Game replay and logging system
- Strategy comparison framework



## Dev Log
- Week 0: Set-up Repo
- Week 1:












