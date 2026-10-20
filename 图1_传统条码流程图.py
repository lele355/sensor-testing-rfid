from graphviz import Digraph

# 创建有向图
dot = Digraph(comment='Traditional Barcode Scanning Flowchart')
# dot.attr(label='图1：传统条码出入库作业流程图', labelloc='b', fontsize='14', fontname='SimHei')
dot.attr('node', shape='box', style='rounded', fontname='SimHei')
dot.attr('edge', fontname='SimHei')
# --- 新增代码：提高图片分辨率 ---
dot.attr(dpi='300')

# 定义节点
dot.node('A', '叉车运送整托盘\n货物至出入库口')
dot.node('B', '作业暂停，\n操作员下车或上前')
dot.node('C', '手持扫描枪\n【逐个】对准货箱条码')
dot.node('D', '扫描一个条码', shape='oval', style='filled', color='lightgrey')
dot.node('E', '是否所有条码\n扫描完毕？', shape='diamond')
dot.node('F', '数据批量导入或\n手动录入WMS系统')
dot.node('G', '叉车继续作业')

# 定义流程
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'D', label='否')
dot.edge('E', 'F', label='是')
dot.edge('F', 'G')

# 生成图片
try:
    file_path = dot.render('barcode_flowchart', format='png', view=False, cleanup=True)
    print(f"流程图 'barcode_flowchart.png' 已成功生成。")
except Exception as e:
    print(f"生成流程图失败，请确保Graphviz软件已正确安装并配置好环境变量。错误信息: {e}")

