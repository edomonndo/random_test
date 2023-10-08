import subprocess
import filecmp
import settings

num_testcase = settings.num_testcase
input_dir = settings.input_dir
naive_dir = settings.naive_dir
out_dir = settings.out_dir
naive_cmd = settings.naive_command
main_cmd = settings.main_command

for i in range(num_testcase):
    f = f"{i:04d}.txt"

    # Run naive solution
    io_cmd = f" < {input_dir}{f} > {naive_dir}{f}"
    subprocess.run(naive_cmd + io_cmd, shell=True)

    # Run main solution
    io_cmd = f" < {input_dir}{f} > {out_dir}{f}"
    subprocess.run(main_cmd + io_cmd, shell=True)

    # Compare results
    res = filecmp.cmp(f"{naive_dir}{f}", f"{out_dir}{f}", shallow=True)
    if not res:
        print(f, res)
print("Done.")
