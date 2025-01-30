<p align="center">
    <img src="https://sacredgraph.com/sacredgraph.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">SchDoc Parser API</h1></p>
<p align="center">
	<em><code>Rest API to convert .SchDoc files into JSON representation</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/SacredGraph/schdoc-parsing-api?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/SacredGraph/schdoc-parsing-api?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/SacredGraph/schdoc-parsing-api?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/SacredGraph/schdoc-parsing-api?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## Table of Contents

- [ Overview](#-overview)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

## Overview

<code>The project's goal is to allow converting .SchDoc files on the fly into a json format.</code>

---

## Project Structure

```sh
└── schdoc-parsing-api/
    ├── LICENSE
    ├── README.md
    ├── altium_schematic_parser
    │   ├── __init__.py
    │   └── parse.py
    ├── requirements.txt
    ├── main.py
    ├── setup.py
    └── tests
        └── altium_crap
```

### Project Index

<details open>
	<summary><b><code>SCHDOC-PARSING-API/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/SacredGraph/schdoc-parsing-api/blob/master/requirements.txt'>requirements.txt</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/SacredGraph/schdoc-parsing-api/blob/master/main.py'>main.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/SacredGraph/schdoc-parsing-api/blob/master/setup.py'>setup.py</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- altium_schematic_parser Submodule -->
		<summary><b>altium_schematic_parser</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/SacredGraph/schdoc-parsing-api/blob/master/altium_schematic_parser/parse.py'>parse.py</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

Before getting started with schdoc-parsing-api, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Install schdoc-parsing-api using one of the following methods:

**Build from source:**

1. Clone the schdoc-parsing-api repository:

```sh
❯ git clone https://github.com/SacredGraph/schdoc-parsing-api
```

2. Navigate to the project directory:

```sh
❯ cd schdoc-parsing-api
```

3. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

### Usage

Run schdoc-parsing-api using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python main.py
```

### Testing

Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```
