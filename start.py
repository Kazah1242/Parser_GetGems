import subprocess

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error #1 {script_name}: {result.stderr}")

def main():
    scripts = [
        'the parser.py', #в терминал отправить url 
        'link.py', #еще пока что прогресс если запустить отсюда не отображается
        'nft img.py',
        'nft metadata.py',
        'fNFT_img.py',
        'covect.py',
        'im boobs.py',
        'lohatron.py',
    ]
    
    for script in scripts:
        run_script(script)  # Запуск каждого скрипта по очереди

if __name__ == "__main__":
    main()