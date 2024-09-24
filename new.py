import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bio as dashbio

# Dash 애플리케이션 생성
app = dash.Dash(__name__)

# 레이아웃 정의
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a PDB File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    dashbio.NglMoleculeViewer(
        id='ngl-viewer',
        stageParameters={'backgroundColor': 'white'},
        modelData=''
    )
])


# 파일 업로드 콜백 정의
@app.callback(
    Output('ngl-viewer', 'modelData'),
    [Input('upload-data', 'contents')]
)
def display_pdb(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        return content_string
    return None


# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)