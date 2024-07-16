# DLCore

DLCore is a personal deep learning project template aimed at facilitating quick setup and execution of deep learning experiments.

## Directory Structure

```
.
├── config
│   └── default.yaml      # Personal default configuration
├── data                  # Data storage directory
├── main.py               # Main program entry point
└── src
    ├── model             # Model definitions
    ├── train.py          # Training logic
    └── utils.py          # Utility functions
```

## Getting Started

### 1. Configuration

- Modify `config/default.yaml` to customize personal configurations.
- Use `--config` argument to specify alternative configuration files.

### 2. Running the Main Program

```bash
python main.py --config config/default.yaml --dataset your_dataset --backup --name experiment_name --data data_directory --src source_directory --log log_directory --output output_directory
```

#### Arguments:

- `--config`: Path to the configuration file.
- `--dataset`: Specify the dataset name.
- `--backup`: Optionally backup code and configurations.
- `--name`: Name of the experiment (default format: YYMMDDHHMMSS).
- `--data`: Path to the data directory.
- `--src`: Path to the source code directory.
- `--log`: Path to the log directory.
- `--output`: Path to the output directory.

### 3. Training Models

Customize `train.py` for specific training requirements.

### 4. Backup

Utilize `--backup` flag for code and configuration backup.