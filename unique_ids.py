#!/usr/bin/env python3

"""
unique_ids.py

Extracts unique tweet IDs from JSON files in a folder
and writes them to a text file.
"""

import json
import os
import sys

def collect_unique_ids(folder_path, output_file):
    unique_ids = set()

    for filename in os.listdir(folder_path):
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(folder_path, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Skipping {filename}: {e}", file=sys.stderr)
            continue

        if "data" not in data or not isinstance(data["data"], list):
            print(f"Skipping {filename}: missing or invalid 'data' field", file=sys.stderr)
            continue

        for tweet in data["data"]:
            if isinstance(tweet, dict) and "id" in tweet:
                tweet_id = tweet["id"].strip()
                if tweet_id:
                    unique_ids.add(tweet_id)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for tid in sorted(unique_ids):
                f.write(tid + "\n")
    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Saved {len(unique_ids)} unique tweet IDs to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 unique_ids.py <folder_path> <output.txt>", file=sys.stderr)
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder", file=sys.stderr)
        sys.exit(1)

    collect_unique_ids(folder_path, output_file)
