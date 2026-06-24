# Java Installation Guide (Ubuntu & macOS)

## Overview

This guide explains how to install Java (OpenJDK) on Ubuntu Linux and macOS, verify the installation, configure `JAVA_HOME`, and manage multiple Java versions.

---

# Ubuntu Installation

## Step 1: Update Package Repository

```bash
sudo apt update
```

## Step 2: Install Java

### Install Java 17 (Recommended)

```bash
sudo apt install openjdk-17-jdk -y
```

### Install Java 21 (Latest LTS)

```bash
sudo apt install openjdk-21-jdk -y
```

---

## Step 3: Verify Installation

```bash
java -version
javac -version
```

Expected Output:

```text
openjdk version "17.x.x"
javac 17.x.x
```

---

## Step 4: Find JAVA_HOME

```bash
readlink -f $(which java)
```

Example Output:

```text
/usr/lib/jvm/java-17-openjdk-amd64/bin/java
```

JAVA_HOME:

```text
/usr/lib/jvm/java-17-openjdk-amd64
```

---

## Step 5: Set JAVA_HOME

Open `.bashrc`:

```bash
nano ~/.bashrc
```

Add the following lines:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

Apply changes:

```bash
source ~/.bashrc
```

Verify:

```bash
echo $JAVA_HOME
```

---

## Step 6: Manage Multiple Java Versions

List installed versions:

```bash
sudo update-alternatives --config java
```

Select the required version from the list.

---

# macOS Installation

## Step 1: Verify Homebrew Installation

```bash
brew --version
```

If Homebrew is not installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## Step 2: Install Java

### Install Java 17

```bash
brew install openjdk@17
```

### Install Java 21

```bash
brew install openjdk@21
```

---

## Step 3: Configure PATH

### Apple Silicon (M1/M2/M3/M4)

```bash
echo 'export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
```

### Intel Mac

```bash
echo 'export PATH="/usr/local/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
```

---

## Step 4: Set JAVA_HOME

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
```

Reload configuration:

```bash
source ~/.zshrc
```

---

## Step 5: Verify Installation

```bash
java -version
javac -version
```

---

## Step 6: View Installed Java Versions

```bash
/usr/libexec/java_home -V
```

Example:

```text
Matching Java Virtual Machines (2):
17.0.15
21.0.7
```

---

## Step 7: Switch Between Java Versions

### Java 17

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
```

### Java 21

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 21)
```

Verify:

```bash
java -version
```

---

# Oracle JDK Installation

Download Oracle JDK from:

https://www.oracle.com/java/technologies/downloads/

Install the downloaded package and verify:

```bash
java -version
javac -version
```

---

# Recommended Versions for Spark Development

| Component     | Version |
| ------------- | ------- |
| Java          | 17 LTS  |
| Scala         | 2.13.16 |
| Spark         | 4.0.0   |
| sbt           | 1.10.x  |
| IntelliJ IDEA | Latest  |

**Note:** Spark 4.0.0 requires Java 17 or later. Avoid Java 8 for Spark 4.x projects.

---

# Quick Verification Commands

```bash
java -version
javac -version
echo $JAVA_HOME
which java
which javac
```

Expected:

```text
Java Runtime Available
Java Compiler Available
JAVA_HOME Configured
Java Executable Path Displayed
Javac Executable Path Displayed
```
