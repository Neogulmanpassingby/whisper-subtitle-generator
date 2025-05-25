import whisper
import os
import sys
import torch



def transcribe_to_srt(video_path):
    # 파일 경로 검사
    if not os.path.exists(video_path):
        print("❌ 파일이 존재하지 않습니다:", video_path)
        return

    # Whisper 모델 로드
    model = whisper.load_model("large")  # 필요시 small, medium, large 가능

    print("🔊 음성 인식 중...")
    result = model.transcribe(video_path)

    # .srt 파일 경로 설정
    base_name = os.path.splitext(video_path)[0]
    srt_path = base_name + ".srt"

    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"]):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            def format_time(seconds):
                h = int(seconds // 3600)
                m = int((seconds % 3600) // 60)
                s = seconds % 60
                return f"{h:02}:{m:02}:{int(s):02},{int((s % 1)*1000):03}"

            f.write(f"{i+1}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(text.strip() + "\n\n")

    print(f"✅ SRT 자막 생성 완료: {srt_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python generate_srt.py 영상파일경로")
        sys.exit(1)
    print("GPU 사용 여부:", torch.cuda.is_available()) 

    video_path = sys.argv[1]
    transcribe_to_srt(video_path)
