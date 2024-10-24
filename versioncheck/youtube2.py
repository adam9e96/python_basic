import os
import googleapiclient.discovery


def get_youtube_data(api_key, channel_ids):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    table_rows = ""
    for channel_id in channel_ids:
        request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        response = request.execute()

        for item in response['items']:
            channel_title = item['snippet']['title']
            subscriber_count = int(item['statistics']['subscriberCount'])
            video_count = int(item['statistics']['videoCount'])
            view_count = int(item['statistics']['viewCount'])

            avg_views_per_video = view_count / video_count if video_count > 0 else 0
            views_per_subscriber = view_count / subscriber_count if subscriber_count > 0 else 0

            table_rows += f"""
            <tr>
                <td>{channel_title}</td>
                <td>{subscriber_count}</td>
                <td>{video_count}</td>
                <td>{view_count}</td>
                <td>{avg_views_per_video:.2f}</td>
                <td>{views_per_subscriber:.2f}</td>
            </tr>
            """

    with open("youtube_data.html", "w", encoding="utf-8") as file:
        file.write(html_template.replace("{{table_rows}}", table_rows))


if __name__ == "__main__":
    API_KEY = "AIzaSyBYo6KRiC04EGDqW2XLdlWsyxgsjF-AJew"
    CHANNEL_IDS = [
        "UCAHVQ44O81aehLWfy9O6Elw",
        "UC7-m6jQLinZQWIbwm9W-1iw",
        "UC_eeSpMBz8PG4ssdBPnP07g",
        "UC1afpiIuBDcjYlmruAa0HiA",
        "UClbYIn9LDbbFZ9w2shX3K0g",
        "UCKzfyYWHQ92z_2jUcSABM8Q",
        "UCIVFv8AiQLqM9oLHTixrNYw",
        "UC2b4WRE5BZ6SIUWBeJU8rwg",
        "UCYxLMfeX1CbMBll9MsGlzmw",
        "UCQmcltnre6aG9SkDRYZqFIg",
        "UCcA21_PzN1EhNe7xS4MJGsQ",
        "UCj0c1jUr91dTetIQP2pFeLA",
    ]

    html_template = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>YouTube Channel Data</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">YouTube Channel Data</h1>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">채널</th>
                        <th scope="col">구독자 수</th>
                        <th scope="col">영상 수</th>
                        <th scope="col">조회 수</th>
                        <th scope="col">영상 당 평균 조회수</th>
                        <th scope="col">구독자 수당 조회수</th>
                    </tr>
                </thead>
                <tbody>
                    {{table_rows}}
                </tbody>
            </table>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    get_youtube_data(API_KEY, CHANNEL_IDS)
