import argparse
import subprocess
import os
import sys
import shlex
import json


def run_eval(ckpt: str):
    ckpt_name = os.path.basename(ckpt)
    dp_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "diffusion_policy"))
    output_dir = os.path.join(os.path.dirname(ckpt), "evals", ckpt_name.removesuffix(".ckpt"))
    cmd = f"python {dp_dir}/eval.py --checkpoint {ckpt} -o {output_dir}"
    if not os.path.exists(output_dir):
        try:
            subprocess.check_call(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Error: Evaluation subprocess failed with exit code {e.returncode}", file=sys.stderr)
            raise

    with open(os.path.join(output_dir, "eval_log.json"), "r") as f:
        results = json.load(f)
        mean_score = results["test/mean_score"]
        success_rate = sum(float(results[f"test/sim_max_reward_1000{i:02}"]) >= 0.95 for i in range(50)) / 50

    return mean_score, success_rate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, required=True)
    args = parser.parse_args()

    ckpt_dir = os.path.join(args.exp, "checkpoints")
    total_mean_score = 0
    total_success_rate = 0
    num_exps = 0
    for ckpt_name in sorted(os.listdir(ckpt_dir))[1:]:
        if not ckpt_name.endswith(".ckpt"):
            continue
        ckpt = os.path.join(ckpt_dir, ckpt_name)
        mean_score, success_rate = run_eval(ckpt)
        total_mean_score += mean_score
        total_success_rate += success_rate
        num_exps += 1

    avg_mean_score = total_mean_score / num_exps
    avg_success_rate = total_success_rate / num_exps

    print(f"{avg_mean_score=:.4f}, {avg_success_rate=:.4f}")


if __name__ == "__main__":
    main()