# PrintQueue

PrintQueue is a Python program designed to manage and organize printing tasks on Windows systems. It aims to streamline the printing process and reduce wait times by efficiently handling multiple print jobs.

## Features

- Add print jobs with a specific number of pages.
- Simulate processing of print jobs with a given time delay.
- Automatically process jobs in the order they are added to the queue.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/PrintQueue.git
   ```
2. Navigate to the project directory:
   ```sh
   cd PrintQueue
   ```

### Usage

Run the `print_queue.py` script to start the print queue manager:

```sh
python print_queue.py
```

You can add print jobs by modifying the `main()` function in `print_queue.py`. The example provided in the script adds several print jobs to demonstrate the functionality.

### Example

```python
print_queue.add_job(PrintJob("Document1", 5))
print_queue.add_job(PrintJob("Document2", 3))
print_queue.add_job(PrintJob("Document3", 10))
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to efficiently manage print tasks in busy environments.
- Built with Python's threading and queue libraries to handle concurrent tasks.