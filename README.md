# VSCO Downloader API - Images and Videos

![image](https://user-images.githubusercontent.com/63386979/187305982-6aec5669-13d7-4a3c-a411-add1d0912bf1.png)

Super simple API takes in a link to a VSCO image or photo and downloads it for the client.

## How to Use
#### POST `/fetchObject`
- takes in json body of image/photo link

Example
```json
{
  "link": "https://vsco.co/allentran/media/5f3779c092f1e1320f8cd973"
}
