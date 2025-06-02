# Simple Whisper Subtitle Generator

이 스크립트는 [OpenAI Whisper](https://github.com/openai/whisper)를 사용하여 비디오 파일로부터 자동으로 자막(SRT 파일)을 생성해주는 CLI 도구입니다.

## ✅ 기능

- Whisper를 사용한 고정밀 음성 인식
- `.mp4`, `.mkv` 등 다양한 비디오 포맷 지원
- 결과물은 영상과 동일한 이름의 `.srt` 자막 파일로 저장됨
- GPU 사용 가능 시 자동 활용
- 추후 GUI 추가예정
---

## 🔧 설치 방법

Python 3.8 이상이 필요합니다.

```bash
git clone https://github.com/yourusername/simple-whisper-subtitle-generator.git
cd simple-whisper-subtitle-generator
pip install -r requirements.txt
```
> ※ `torch` 및 `whisper` 패키지가 포함되어 있으며, **CUDA 지원 GPU**가 있다면 **GPU 가속이 자동으로 사용**됩니다.  
> ※ Whisper의 **`large` 모델은 약 2GB**의 모델 파일을 다운로드하므로, **처음 실행 시 시간이 오래 걸릴 수 있습니다**.

---

## ▶️ 사용법

```bash
python generate_srt.py [영상파일 경로]

