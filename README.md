*This project has been created as part of the 42 curriculum by vafechte, matdos-s.*

## Description
A-Maze-ing is a Python-based maze generator that creates, solves, and visually displays random mazes. The goal of this project is to explore procedural generation, graph theory (BFS/DFS), and modern Python packaging. It can generate perfect mazes (containing exactly one valid path between the entry and exit) and outputs the internal structure into a hexadecimal text file.

## Instructions

### Prerequisites
* Python 3.10 or later
* `make`

### Installation & Execution
You can use the provided `Makefile` to easily setup and run the project:

1. **Install dependencies and the local package:**
   ```bash
   make install
   ```
2. **Run the program:**
   ```bash
   make run
   # Or manually: python3 a_maze_ing.py config.txt
   ```
3. **Build the distributable package (.whl / .tar.gz):**
   ```bash
   make build_package
   ```
4. **Clean cache and artifacts:**
   ```bash
   make clean
   ```

## Configuration File Format
The program requires a `config.txt` file passed as an argument. The file uses `KEY=VALUE` pairs. Lines starting with `#` are ignored.

**Mandatory Keys:**
* `WIDTH`: Width of the maze in cells (int)
* `HEIGHT`: Height of the maze in cells (int)
* `ENTRY`: X,Y coordinates for the start (e.g., `0,0`)
* `EXIT`: X,Y coordinates for the end (e.g., `19,14`)
* `OUTPUT_FILE`: Must be `maze.txt`
* `PERFECT`: `True` or `False` (generates a single-path maze)

**Example `config.txt`:**
```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
```

## Maze Generation Algorithm
* **Algorithm Used:** Randomized Depth-First Search (Iterative Implementation)
* **Why we chose it:** This algorithm is excellent for generating "perfect" mazes because it carves paths by visiting every cell exactly once, naturally preventing isolated areas or loops. By using an iterative stack approach (tracking the path array) rather than deep recursion, we prevent stack-overflow errors on very large maze dimensions. It also tends to generate long, winding corridors which makes the maze visually interesting.

## Code Reusability (`mazegen` Package)
The core maze logic has been decoupled into a standalone, pip-installable module named `mazegen`. 

* **Instantiate the generator & Pass custom parameters:**
  You can import the `MazeGenerator` class and pass the size and an optional seed for reproducibility.
  ```python
  from mazegen import MazeGenerator
  
  # Initialize with custom width, height, and seed
  gen = MazeGenerator(width=20, height=15, seed=42)
  ```
* **Generate the structure:**
  ```python
  gen.generate(entry=(0,0))
  ```
* **Access the generated structure:**
  The internal grid is accessible via `gen.maze`, which is a 2D list of `Cellule` objects containing coordinate and wall data.
* **Access a solution:**
  You can solve the maze using Breadth-First Search (BFS) by calling:
  ```python
  solution_string = gen.solve(entry=(0,0), exit_coords=(19,14))
  # Returns a string of directions like: 'SWSESW...'
  ```

## Team and Project Management
* **Roles:**
* **vafechte:** Focused on the core maze generation algorithm (_get_random_unvisited_neighbor, init_maze, open_walls, save_to_hex_file),
the BFS solver logic, the parsing file and structuring the `mazegen` Python package architecture.
* **matdos-s:** Focused on the visual representation and on the dfs algorith,  specifically designing the terminal display logic (`print_maze.py`) and bitwise wall rendering.
* **Anticipated Planning vs. Reality:** We initially planned to build the entire script in one file and separate it later. However, we realized that merging different data structures (objects vs. binary strings) at the end was tricky. We adapted by using the Adapter design pattern (`get_binary_maze()`) to safely connect the generator to the display logic without rewriting each other's code.
* **What worked well:** Dividing the logic (Generation vs. Display) allowed us to work in parallel without merge conflicts.
* **What could be improved:** We could have agreed on a strict internal data structure on day one to avoid needing an adapter later.
* **Tools Used:** Git/GitHub for version control, `hatchling` and `build` for Python packaging, Mypy for static typing, and Flake8 for linting.

## Resources
* **References:** * [Maze generation algorithms (Wikipedia)](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
  * [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
  * [Adapter Design Pattern](https://refactoring.guru/design-patterns/adapter)
* **AI Usage:** We used an AI assistant (Gemini) primarily as a technical sounding board and refactoring tool. Specifically, it was used to:
  1. Understand how to write a standard `pyproject.toml` and restructure our flat scripts into a pip-installable package (`mazegen/`).
  2. Help design an Adapter method to bridge the gap between `MazeGenerator`'s object-oriented data and `print_maze.py`'s binary string expectations.
  3. Format this README to ensure compliance with the school's strict evaluation guidelines.
