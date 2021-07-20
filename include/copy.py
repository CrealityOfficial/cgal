from pathlib import Path
import shutil

def process():
    sourcePath = Path("F:/BaiduNetdiskDownload/baiwenlei-gitee-cgal-master/cgal/")
    current_path = Path.cwd()
    for d in sourcePath.iterdir():
        name = d.stem
        inDir = d.joinpath("include")
        if inDir.exists():
            print(inDir)
            shutil.copytree(inDir, current_path.joinpath(name))
    
def delete():
    for d in Path('.').iterdir():
        if(d.is_dir()):
            shutil.rmtree(d)
            
def run():
    delete()
    process()
            
if __name__ == "__main__":
    run()