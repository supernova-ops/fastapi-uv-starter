# 1. 소스 코드를 담을 'app' 폴더 생성
mkdir -p backend/app

# 2. 파이썬 파일들을 'app' 안으로 이동
mv backend/main.py backend/schemas.py backend/app/

# 3. 'app' 폴더를 파이썬 패키지로 만들기 위해 빈 파일 생성
touch backend/app/__init__.py

# 4. 루트에 남은 찌꺼기 폴더 삭제
rm -rf __pycache__

# 5. (선택) 중복된 문서 파일 삭제
rm "docs/guides/installation copy.md"

# 6. 최종 확인
tree -L 3
