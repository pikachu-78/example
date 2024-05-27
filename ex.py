import sys

print("hello word")
def main():
    changed_files = sys.argv[1]
    print(f"Changed files: {changed_files}")

if __name__ == "__main__":
    main()
