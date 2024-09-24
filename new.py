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
    app.run_server(debug=import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bio as dashbio

# PDB 파일 경로를 지정합니다.
pdb_file_path = "path_to_your_pdb_file.pdb"  # 여기에 PDB 파일의 경로를 입력하세요.

# PDB 파일을 읽어서 문자열로 변환합니다.
def read_pdb_file(file_path):
    with open(file_path, 'r') as file:
        pdb_string = file.read()
    return pdb_string

# Dash 애플리케이션 생성
app = dash.Dash(__name__)

# 레이아웃 정의
app.layout = html.Div([
    html.Div([
        html.Label("PDB File Path:"),
        dcc.Input(id='pdb-file-path', value=pdb_file_path, type='text', style={'width': '70%'}),
        html.Button('Load PDB', id='load-pdb-button', n_clicks=0),
    ], style={'padding': '20px'}),
    
    dashbio.NglMoleculeViewer(
        id='ngl-viewer',
        height='600px',
        width='100%',
        data=''
    )
])

# PDB 파일 경로를 사용하여 PDB 데이터를 로드하고 시각화하는 콜백
@app.callback(
    Output('ngl-viewer', 'data'),
    [Input('load-pdb-button', 'n_clicks')],
    [dash.dependencies.State('pdb-file-path', 'value')]
)
def update_viewer(n_clicks, pdb_path):
    if n_clicks > 0 and pdb_path:
        pdb_data = read_pdb_file(pdb_path)
        return pdb_data
    return ''


# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)  






TypeError: The `dash_bio.NglMoleculeViewer` component (version 1.0.2) with the ID "ngl-viewer" received an unexpected keyword argument: `modelData`
Allowed arguments: data, downloadImage, height, id, imageParameters, loading_state, molStyles, pdbString, stageParameters, width
