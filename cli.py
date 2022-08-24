from typing import Optional

import typer
import uvicorn

app = typer.Typer()


@app.command()
def run(reload: Optional[bool] = False):
    uvicorn.run('main:app', host='0.0.0.0', port=8003, headers=[('server', 'ggl')], reload=reload, http='h11')


if __name__ == '__main__':
    app()
