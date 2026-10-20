from graphviz import Digraph

# --- 创建高清流程图 ---
dot = Digraph(comment='RFID System Architecture', graph_attr={'dpi': '300', 'rankdir': 'LR', 'nodesep': '0.8'})
dot.attr('node', shape='box', style='rounded,filled', fontname='SimHei', fontsize='10')
dot.attr('edge', fontname='SimHei', fontsize='9')

# --- 定义硬件层 ---
with dot.subgraph(name='cluster_hardware') as c:
    c.attr(label='硬件层', fontname='SimHei', style='rounded', color='black')
    c.node('tag', 'RFID电子标签\n(贴于货物)', fillcolor='ivory')
    c.node('reader', '固定式读写器\n+ 天线 (通道门)', fillcolor='lightgreen', width='2.5')
    c.node('alarm', '声光报警器', shape='ellipse', fillcolor='orangered', style='filled', fontcolor='white', width='2')
    # 辅助节点用于对齐
    dot.node('align_node', '', style='invis', width='0.1')
    
# --- 定义软件/系统层 ---
with dot.subgraph(name='cluster_software') as c:
    c.attr(label='软件/系统层', fontname='SimHei', style='rounded', color='black')
    c.node('middleware', '数据中间件\n(过滤/处理)', fillcolor='yellow', width='2.5')
    c.node('wms', '仓库管理系统 (WMS)\n(业务逻辑/数据库)', fillcolor='lightblue', width='3')

# --- 定义数据流 ---
dot.edge('tag', 'reader', label='无线射频信号')
dot.edge('reader', 'middleware', label=' 原始标签数据')
dot.edge('middleware', 'wms', label=' 有效业务数据')
dot.edge('wms', 'alarm', label=' 触发异常指令', style='dashed', constraint='false')

# --- 使用不可见的边来辅助布局对齐 ---
dot.edge('reader', 'align_node', style='invis')
dot.edge('align_node', 'alarm', style='invis')


# --- 输出文件 ---
try:
    file_path = dot.render('system_structure_diagram', format='png', view=False, cleanup=True)
    print(f"高清优化版'system_structure_diagram.png'已成功生成。")
except Exception as e:
    print(f"生成流程图失败，请确保Graphviz软件已正确安装并配置好环境变量。错误信息: {e}")

