import argparse
import subprocess
import os
import sys
import shlex
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True)
    args = parser.parse_args()

    dp_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "diffusion_policy"))
    ckpt_dir = os.path.dirname(os.path.abspath(args.checkpoint))
    ckpt_name = args.checkpoint.split("/")[-1].split(".")[0]
    output_dir = os.path.join(ckpt_dir, f"eval_{ckpt_name}")
    cmd = f"python {dp_dir}/eval.py --checkpoint {args.checkpoint} -o {output_dir}"
    subprocess.check_call(shlex.split(cmd), stdout=sys.stdout, stderr=sys.stderr)
    with open(os.path.join(output_dir, "eval_log.json"), "r") as f:
        results = json.load(f)
        mean_score = results["test/mean_score"]
        success_rate = sum(float(results[f"test/sim_max_reward_1000{i:02}"]) >= 0.95 for i in range(50)) / 50
        print(f"{mean_score=:.4f}, {success_rate=:.4f}")

if __name__ == "__main__":
    main()