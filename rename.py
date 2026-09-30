"""
批量重命名工具
用法示例：
  python rename.py ./照片 --mode replace --old "IMG_" --new "旅行_"
  python rename.py ./照片 --mode prefix --prefix "2026_"
  python rename.py ./照片 --mode number --start 1
不加 --apply 只预览，加了才真正执行改名。
"""
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="批量重命名文件")
    parser.add_argument("folder", help="要处理的文件夹路径")
    parser.add_argument(
        "--mode",
        required=True,
        choices=["replace", "prefix", "suffix", "number"],
        help="replace=替换文字, prefix=加前缀, suffix=加后缀, number=按序号",
    )
    parser.add_argument("--old", default="", help="replace模式：要被替换的文字")
    parser.add_argument("--new", default="", help="replace模式：替换成的文字")
    parser.add_argument("--prefix", default="", help="prefix模式：要加的前缀")
    parser.add_argument("--suffix", default="", help="suffix模式：要加的后缀")
    parser.add_argument("--start", type=int, default=1, help="number模式：起始序号")
    parser.add_argument("--apply", action="store_true", help="真正执行（不加则只预览）")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"错误：找不到文件夹 {args.folder}")
        return

    files = sorted(
        f
        for f in os.listdir(args.folder)
        if os.path.isfile(os.path.join(args.folder, f))
    )
    print(f"共找到 {len(files)} 个文件，预览如下：\n")

    renamed = 0
    for i, old_name in enumerate(files):
        name, ext = os.path.splitext(old_name)
        if args.mode == "replace":
            new_name = name.replace(args.old, args.new) + ext
        elif args.mode == "prefix":
            new_name = args.prefix + old_name
        elif args.mode == "suffix":
            new_name = name + args.suffix + ext
        elif args.mode == "number":
            new_name = f"file_{args.start + i:03d}{ext}"
        else:
            continue

        if new_name == old_name:
            continue

        print(f"  {old_name}  ->  {new_name}")
        renamed += 1

        if args.apply:
            src = os.path.join(args.folder, old_name)
            dst = os.path.join(args.folder, new_name)
            if os.path.exists(dst):
                print(f"  跳过（目标已存在）：{new_name}")
                continue
            os.rename(src, dst)

    print(f"\n共 {renamed} 个文件需要改名。")
    if not args.apply:
        print("以上仅为预览。确认无误后加 --apply 参数真正执行。")
    else:
        print("已完成。")


if __name__ == "__main__":
    main()
