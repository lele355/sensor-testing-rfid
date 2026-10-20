from graphviz import Digraph

# 创建一个有向图对象
dot = Digraph(comment='RFID Data Reading Flowchart')
# dot.attr(label='图3：RFID数据读取工作流程', labelloc='b', fontsize='14', fontname='SimHei')
dot.attr('node', shape='box', style='rounded', fontname='SimHei')
dot.attr('edge', fontname='SimHei')
# --- 新增代码：提高图片分辨率 ---
dot.attr(dpi='300')

# 定义流程中的节点
dot.node('A', '读写器通过天线\n发射电磁波形成能量场')
dot.node('B', '贴有标签的货物\n进入电磁场', shape='diamond')
dot.node('C', '标签天线获取能量\n芯片被激活')
dot.node('D', '标签芯片调制ID信息\n通过天线反射信号')
dot.node('E', '读写器天线接收\n经过调制的反射信号')
dot.node('F', '读写器解码信号\n获得标签ID数据')
dot.node('G', '将ID数据上传\n至后台系统')

# 定义流程的边（连接）
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')

# 生成流程图
try:
    file_path = dot.render('rfid_flowchart', format='png', view=False, cleanup=True)
    print(f"流程图 'rfid_flowchart.png' 已成功生成。")
except Exception as e:
    print(f"生成流程图失败，请确保Graphviz软件已正确安装并配置好环境变量。错误信息: {e}")

