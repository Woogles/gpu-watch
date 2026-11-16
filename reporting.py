from datetime import datetime

from config import REPORT_DIR


def generate_report(
    listings
):

    rows = []

    for item in listings:

        rows.append(
            f"""
            <tr>
              <td>{item.source}</td>
              <td>{item.gpu_name}</td>
              <td>${item.price:.2f}</td>
              <td>{item.condition}</td>
              <td>
              <a href="{item.url}">
              View
              </a>
              </td>
            </tr>
            """
        )

    html = f"""
    <html>
    <body>

    <h1>GPU Watch Report</h1>

    <table border="1">

    <tr>
      <th>Source</th>
      <th>GPU</th>
      <th>Price</th>
      <th>Condition</th>
      <th>Link</th>
    </tr>

    {''.join(rows)}

    </table>

    </body>
    </html>
    """

    REPORT_DIR.mkdir(
        exist_ok=True
    )

    filename = (
        REPORT_DIR /
        f"report_{datetime.now():%Y%m%d}.html"
    )

    filename.write_text(
        html,
        encoding="utf-8"
    )

    return html