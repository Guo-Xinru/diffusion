import sys
import platform
from pathlib import Path

def try_import(name):
    try:
        mod = __import__(name)
        return mod
    except Exception as e:
        return None

def main():
    print("=== Diffusion project smoke test ===")
    print(f"Python: {sys.version.split()[0]}  ({platform.system()} {platform.release()})")
    print(f"Executable: {sys.executable}")
    print(f"Project root: {Path(__file__).resolve().parents[2]}")

    # numpy
    np = try_import("numpy")
    print("NumPy:", np.__version__ if np else "not installed")

    # torch (optional)
    torch = try_import("torch")
    if torch:
        print("PyTorch:", torch.__version__)
        print("CUDA available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("CUDA device count:", torch.cuda.device_count())
            print("CUDA device 0:", torch.cuda.get_device_name(0))
    else:
        print("PyTorch: not installed")

    print("All good ✅")

if __name__ == "__main__":
    main()