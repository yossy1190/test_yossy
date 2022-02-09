### 商品クラス
from re import I


class Item:
    # コンストラクタ　商品コード、商品名、価格
    # それぞれの引数がインスタンスのアトリビュートに代入される
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        # self.item_list=[item_code,item_name,price]
    
    # 価格を取得するメソッド
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    # コンストラクタ　
    # 商品オーダーリストとして空のリストを作る。買い物かごのイメージ。
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    # 注文した商品を商品注文リスト（買い物かご）にappendしていく
    def add_item_order(self,item_code,item_name,price):
        self.item_order_list.append(item_code)
        # self.item_order_list.append(item_name)
        # self.item_order_list.append(price)
    
    #買い物かご中の商品コードを１つ１つprintしていく 
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

    
    
### メイン処理　関数main
def main():
    # マスタ登録　item_masterという空のリストを作成。Itemクラスを内部でインスタンス化させて、その内容をitem_masterにappendしている。
    # そのお店の商品一覧をここで初期設定したイメージ。
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    # オーダークラスのインスタンス化。上のitem_master配列の中身をコンストラクタに代入。
    order=Order(item_master)
    # オーダークラス内のadd_item_orderメソッドを実行。商品コードを追加していく。
    order.add_item_order("001","りんご",100)

    # オーダー表示
    # オーダークラス内のview_item_listを実行
    order.view_item_list()
    
if __name__ == "__main__":
    main()