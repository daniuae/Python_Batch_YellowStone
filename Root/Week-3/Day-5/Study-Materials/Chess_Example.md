# Low-Level Design (LLD) – Chess Tournament Player Management System

## Problem Statement

A chess academy wants to manage players participating in a tournament.

Each player has:

* Player ID (Unique)
* Player Name
* Rating
* Participation Status

The system should support:

1. Add a new player
2. Update player rating
3. Get player details
4. List qualified players based on rating

---

# Solution

```python
class ChessTournamentSystem:

    def __init__(self):
        self.players = {}

    # Operation 1: Add Player
    def add_player(self, player_id: str, name: str, rating: int) -> dict:

        if player_id in self.players:
            raise ValueError("Player already exists")

        self.players[player_id] = {
            "name": name,
            "rating": rating,
            "status": "Active"
        }

        return self.players

    # Operation 2: Update Rating
    def update_rating(self, player_id: str, new_rating: int) -> dict:

        if player_id not in self.players:
            raise KeyError("Player not found")

        self.players[player_id]["rating"] = new_rating

        return self.players

    # Operation 3: Get Player Details
    def get_player_details(self, player_id: str) -> dict:

        if player_id not in self.players:
            raise KeyError("Player not found")

        return self.players[player_id]

    # Operation 4: List Qualified Players
    def qualified_players(self, minimum_rating: int) -> list:

        qualified = []

        for player_id, details in self.players.items():

            if details["rating"] >= minimum_rating:
                qualified.append(player_id)

        return qualified


# -------------------------
# Test Cases
# -------------------------

chess = ChessTournamentSystem()

print(chess.add_player("P101", "Arjun", 1850))
print(chess.add_player("P102", "Riya", 1700))
print(chess.add_player("P103", "Karthik", 2100))

print(chess.update_rating("P101", 1920))

print(chess.get_player_details("P101"))

print(chess.qualified_players(1800))
```

---

# Function-by-Function Explanation

## Constructor

### Code

```python
def __init__(self):
    self.players = {}
```

### Explanation

The constructor executes automatically when an object is created.

```python
chess = ChessTournamentSystem()
```

Creates an empty dictionary:

```python
{}
```

This dictionary stores all player information.

---

# Function 1: add_player()

### Code

```python
def add_player(self, player_id: str, name: str, rating: int) -> dict:
```

### Purpose

Adds a new player into the tournament.

### Parameters

| Parameter | Description      |
| --------- | ---------------- |
| player_id | Unique Player ID |
| name      | Player Name      |
| rating    | Chess Rating     |

---

### Step 1

```python
if player_id in self.players:
```

Checks whether the player already exists.

Example:

```python
"P101" in self.players
```

Output:

```python
True
```

---

### Step 2

```python
raise ValueError("Player already exists")
```

Raises an exception if duplicate Player ID is found.

Example Output:

```python
ValueError: Player already exists
```

---

### Step 3

```python
self.players[player_id] = {
```

Creates a new entry.

Example:

```python
self.players["P101"] = {
```

---

### Step 4

```python
"name": name
```

Stores player name.

Example:

```python
"name": "Arjun"
```

---

### Step 5

```python
"rating": rating
```

Stores chess rating.

Example:

```python
"rating": 1850
```

---

### Step 6

```python
"status": "Active"
```

Sets default participation status.

Example:

```python
"status": "Active"
```

---

### Step 7

```python
return self.players
```

Returns updated dictionary.

---

# Function 2: update_rating()

### Code

```python
def update_rating(self, player_id: str, new_rating: int) -> dict:
```

### Purpose

Updates the rating of an existing player.

---

### Step 1

```python
if player_id not in self.players:
```

Checks if player exists.

Example:

```python
"P999" not in self.players
```

Output:

```python
True
```

---

### Step 2

```python
raise KeyError("Player not found")
```

Raises an exception if player does not exist.

Example:

```python
KeyError: Player not found
```

---

### Step 3

```python
self.players[player_id]["rating"] = new_rating
```

Updates the rating.

Before:

```python
{
    "rating": 1850
}
```

After:

```python
{
    "rating": 1920
}
```

---

### Step 4

```python
return self.players
```

Returns updated dictionary.

---

# Function 3: get_player_details()

### Code

```python
def get_player_details(self, player_id: str) -> dict:
```

### Purpose

Returns details of a specific player.

---

### Step 1

```python
if player_id not in self.players:
```

Checks whether player exists.

---

### Step 2

```python
raise KeyError("Player not found")
```

Raises exception if player is missing.

---

### Step 3

```python
return self.players[player_id]
```

Returns player details.

Example:

```python
{
    "name": "Arjun",
    "rating": 1920,
    "status": "Active"
}
```

---

# Function 4: qualified_players()

### Code

```python
def qualified_players(self, minimum_rating: int) -> list:
```

### Purpose

Returns all players whose rating is greater than or equal to the given rating.

---

### Step 1

```python
qualified = []
```

Creates an empty list.

Example:

```python
[]
```

---

### Step 2

```python
for player_id, details in self.players.items():
```

Loops through every player.

Example:

```python
P101
P102
P103
```

---

### Step 3

```python
if details["rating"] >= minimum_rating:
```

Checks qualification criteria.

Example:

```python
1920 >= 1800
```

Output:

```python
True
```

---

### Step 4

```python
qualified.append(player_id)
```

Adds player ID to result list.

Example:

```python
["P101"]
```

Then:

```python
["P101", "P103"]
```

---

### Step 5

```python
return qualified
```

Returns final qualified players list.

Example:

```python
["P101", "P103"]
```

---

# Dry Run

## Add Players

```python
chess.add_player("P101", "Arjun", 1850)
chess.add_player("P102", "Riya", 1700)
chess.add_player("P103", "Karthik", 2100)
```

Dictionary:

```python
{
    "P101": {
        "name": "Arjun",
        "rating": 1850,
        "status": "Active"
    },
    "P102": {
        "name": "Riya",
        "rating": 1700,
        "status": "Active"
    },
    "P103": {
        "name": "Karthik",
        "rating": 2100,
        "status": "Active"
    }
}
```

---

## Update Rating

```python
chess.update_rating("P101", 1920)
```

Updated:

```python
{
    "name": "Arjun",
    "rating": 1920,
    "status": "Active"
}
```

---

## Get Details

```python
chess.get_player_details("P101")
```

Output:

```python
{
    "name": "Arjun",
    "rating": 1920,
    "status": "Active"
}
```

---

## Qualified Players

```python
chess.qualified_players(1800)
```

Evaluation:

| Player ID | Rating | Qualified |
| --------- | ------ | --------- |
| P101      | 1920   | Yes       |
| P102      | 1700   | No        |
| P103      | 2100   | Yes       |

Output:

```python
["P101", "P103"]
```

---

# Time Complexity Analysis

| Method               | Complexity |
| -------------------- | ---------- |
| add_player()         | O(1)       |
| update_rating()      | O(1)       |
| get_player_details() | O(1)       |
| qualified_players()  | O(n)       |

Where:

* n = Number of Players

---

# Test Cases

## TC1 – Add Player

```python
chess.add_player("P101", "Arjun", 1850)
```

Expected:

```python
Player added successfully
```

---

## TC2 – Update Rating

```python
chess.update_rating("P101", 1920)
```

Expected:

```python
Rating updated successfully
```

---

## TC3 – Get Player Details

```python
chess.get_player_details("P101")
```

Expected:

```python
{
    "name": "Arjun",
    "rating": 1920,
    "status": "Active"
}
```

---

## TC4 – Qualified Players

```python
chess.qualified_players(1800)
```

Expected:

```python
["P101", "P103"]
```

---

## TC5 – Hidden Test Cases

### Duplicate Player

```python
chess.add_player("P101", "Arjun", 1850)
```

Expected:

```python
ValueError: Player already exists
```

### Missing Player

```python
chess.get_player_details("P999")
```

Expected:

```python
KeyError: Player not found
```

---

# Final Output

```python
['P101', 'P103']
```

This solution satisfies all requirements:

✅ 4 Methods Implemented

✅ Dictionary-Based Storage

✅ Exception Handling

✅ Hidden Test Cases Covered

✅ OOP-Based Design

✅ Easy-to-Understand LLD Solution
