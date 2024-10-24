import os
import googleapiclient.discovery


# https://ytlarge.com/youtube/channel-id-finder/ko
def get_youtube_data(api_key, channel_ids):
    # 로컬에서 실행할 때 OAuthlib의 HTTPS 검증을 비활성화합니다.
    # *생산 환경에서는 이 옵션을 활성화하지 마세요.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # YouTube API 클라이언트 생성
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # 각 채널에 대한 데이터 가져오기
    for channel_id in channel_ids:
        request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        response = request.execute()

        # print(response)

        # 관련 정보 추출
        for item in response['items']:
            channel_title = item['snippet']['title']
            subscriber_count = int(item['statistics']['subscriberCount'])
            video_count = int(item['statistics']['videoCount'])
            view_count = int(item['statistics']['viewCount'])

            # 계산
            avg_views_per_video = view_count / video_count if video_count > 0 else 0
            views_per_subscriber = view_count / subscriber_count if subscriber_count > 0 else 0

        print(f"채널: {channel_title}")
        print(f"구독자 수: {subscriber_count}")
        print(f"영상 수: {video_count}")
        print(f"조회 수 : {view_count}")
        print(f"영상 당 평균 조회수: {avg_views_per_video:.2f}")
        print(f"구독자 수당 조회수: {views_per_subscriber:.2f}")
        print("-------------")


if __name__ == "__main__":
    # API 키를 자신의 것으로 교체하세요.
    API_KEY = "AIzaSyBYo6KRiC04EGDqW2XLdlWsyxgsjF-AJew"

    # 데이터를 가져올 채널 ID 목록
    CHANNEL_IDS = [
        "UCAHVQ44O81aehLWfy9O6Elw",  # 아라하시 타비
        "UC7-m6jQLinZQWIbwm9W-1iw",  # 아카네 리제
        "UC_eeSpMBz8PG4ssdBPnP07g",  # 네네코 마시로
        "UC1afpiIuBDcjYlmruAa0HiA",  # 시라유키 히나
        "UClbYIn9LDbbFZ9w2shX3K0g",  # 아야츠노 유니
        "UCKzfyYWHQ92z_2jUcSABM8Q",  # 아이리칸나
        "UCIVFv8AiQLqM9oLHTixrNYw",  # 강지
        "UC2b4WRE5BZ6SIUWBeJU8rwg",  # 공식채널
        "UCYxLMfeX1CbMBll9MsGlzmw",  # 텐코 시부키
        "UCQmcltnre6aG9SkDRYZqFIg",  # 아오쿠모 린
        "UCcA21_PzN1EhNe7xS4MJGsQ",  # 하나코 나나
        "UCj0c1jUr91dTetIQP2pFeLA",  # 유즈하 리코

    ]

    get_youtube_data(API_KEY, CHANNEL_IDS)
