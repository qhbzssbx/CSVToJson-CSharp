import DateOption
import JsonTool
import BuildCSharp


def main():
    json_save_path = r"D:\Project\Unity\RGB_1\Assets\StreamingAssets\Config"
    cs_save_path = r"D:\Project\Unity\RGB_1\Assets\Script\Config"
    # json_save_path = r"D:\Project\Python\ExcelToCSharp\save_path"
    # cs_save_path = r"D:\Project\Python\ExcelToCSharp\save_path"
    date = DateOption.GetDate(r"D:\Project\Unity\RGB_1\excel")
    JsonTool.Start(date, json_save_path)
    BuildCSharp.BuildCSharp(date, cs_save_path)


if __name__ == '__main__':
    main()
