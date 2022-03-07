#もしウィンドウが既に存在している場合はそれを予め削除してからもう一度生成する。
WindowExists = cmds.window ("AnimationCopy" , ex =True)
if WindowExists == True:
    cmds.deleteUI("AnimationCopy")

#ボタン付きGUIの作成

button_window = cmds.window ("AnimationCopy" , bgc = (0.25,0.25,0.25))
button_layout = cmds.columnLayout (adjustableColumn = True , parent = button_window )

#=====
#オブジェクトの選択
#コピー元とコピー先のテキストフィールドの配置
cmds.text(label="Animation_Copy",bgc = (0.15,0.15,0.15),h=25)
buttonE = cmds.button(label = "Copy" , command = "Copy()",parent=button_layout , bgc = (0.35,0.35,0.35),h=50)
cmds.rowLayout( numberOfColumns=6, 
                columnWidth6=(  50, 85 , 30 , 30 , 85 , 30), 
                columnAttach=( (1,'both',0), (2,'both',0),(3,'both',0),(4,'both',0),(5,'both',0),(6,'both',0) ),
                adj=True
              ) 

cmds.text(label="Copy :",h=30)
cmds.textField("CopyOrigin",h=30, tx="" ,ed=False,bgc = (0.15,0.15,0.15)) 
cmds.button("SelectOrigin" ,label="✔",h=30 , command="SelectOrigin()" )
cmds.text(label="to",h=30)
cmds.textField("CopyFocus",h=30, tx="",ed=False,bgc = (0.15,0.15,0.15)) 
cmds.button("SelectFocus" ,label="✔",h=30, command="SelectFocus()")
cmds.setParent(u=True)

cmds.rowLayout( numberOfColumns=3, 
                columnWidth3=(  100, 100 , 100 ), 
                columnAttach=( (1,'both',0), (2,'both',0),(3,'both',0) )
              ) 
cmds.checkBox("translate",h=30,label="translate",v=True)
cmds.checkBox("rotate",h=30,label="rotate",v=True)
cmds.checkBox("scale",h=30,label="scale",v=True)
cmds.setParent(u=True)

#リセットボタンの配置
cmds.button("ResetSelection" ,label="Reset Selection",h=30 , command="ResetSelection()" , bgc = (0.35,0.35,0.35) )

cmds.text(label="")

#ウィンドウを起動する
cmds.showWindow(button_window)



#コピー元のオブジェクトを選択
def SelectOrigin():
    selectobj = cmds.ls(sl=True) 
    selectobj = str(selectobj).replace("['","")
    selectobj = str(selectobj).replace("']","")
    
    copyobj = cmds.textField("CopyFocus", tx=True ,q=True )
    if selectobj == copyobj:
        cmds.error("オブジェクトが被っています。別のオブジェクトを選択してください")
        
    cmds.textField("CopyOrigin", tx=str(selectobj) ,e=True ) 

#コピー先のオブジェクトを選択
def SelectFocus():
    selectobj = cmds.ls(sl=True) 
    selectobj = str(selectobj).replace("['","")
    selectobj = str(selectobj).replace("']","")
    
    originobj = cmds.textField("CopyOrigin", tx=True ,q=True )
    if selectobj == originobj:
        cmds.error("オブジェクトが被っています。別のオブジェクトを選択してください")
    
    cmds.textField("CopyFocus", tx=str(selectobj) ,e=True ) 


#選択オブジェクトのリセット
def ResetSelection():
    cmds.textField("CopyOrigin",text="",e=True)
    cmds.textField("CopyFocus",text="",e=True)

#アニメーションのコピーを行う
def Copy():
    #現在のフレーム値を取っておく
    time = cmds.currentTime(q=True)
    
    #どのアトリビュートをコピーするか
    translateMode = cmds.checkBox("translate",q=True,v=True)
    rotateMode = cmds.checkBox("rotate",q=True,v=True)
    scaleMode = cmds.checkBox("scale",q=True,v=True)
    
    
    #テキストトフィールド内に表示されているオブジェクト
    SelectObj = cmds.textField("CopyOrigin", tx=True ,q=True )
    CopyObj = cmds.textField("CopyFocus", tx=True ,q=True )
    if SelectObj == "":
        cmds.error("オブジェクトを設定してください")
    if CopyObj == "":
        cmds.error("オブジェクトを設定してください")
        
    #キーフレームを検索
    firstframe = cmds.findKeyframe(SelectObj,w="first")
    lastframe = cmds.findKeyframe(SelectObj,w="last")
    
    
    #オブジェクトの最初の位置を取得
    fotx = cmds.getAttr(SelectObj + ".translateX",time = firstframe )
    foty = cmds.getAttr(SelectObj + ".translateY",time = firstframe )
    fotz = cmds.getAttr(SelectObj + ".translateZ",time = firstframe )    
    fftx = cmds.getAttr(CopyObj + ".translateX",time = firstframe )
    ffty = cmds.getAttr(CopyObj + ".translateY",time = firstframe )
    fftz = cmds.getAttr(CopyObj + ".translateZ",time = firstframe )

    #オブジェクトの最初の回転値を取得
    forx = cmds.getAttr(SelectObj + ".rotateX",time = firstframe )
    fory = cmds.getAttr(SelectObj + ".rotateY",time = firstframe )
    forz = cmds.getAttr(SelectObj + ".rotateZ",time = firstframe )    
    ffrx = cmds.getAttr(CopyObj + ".rotateX",time = firstframe )
    ffry = cmds.getAttr(CopyObj + ".rotateY",time = firstframe )
    ffrz = cmds.getAttr(CopyObj + ".rotateZ",time = firstframe )
    
    #オブジェクトの最初の回転値を取得
    fosx = cmds.getAttr(SelectObj + ".scaleX",time = firstframe )
    fosy = cmds.getAttr(SelectObj + ".scaleY",time = firstframe )
    fosz = cmds.getAttr(SelectObj + ".scaleZ",time = firstframe )    
    ffsx = cmds.getAttr(CopyObj + ".scaleX",time = firstframe )
    ffsy = cmds.getAttr(CopyObj + ".scaleY",time = firstframe )
    ffsz = cmds.getAttr(CopyObj + ".scaleZ",time = firstframe )
    
    
    frame = firstframe-1
    while frame < lastframe:
        #キーフレームの検索
        nextframe = cmds.findKeyframe( SelectObj,w="next",time=(frame,frame) )
        #キーフレーム中のオブジェクトの位置をコピー
        if translateMode ==True:
            #キーフレーム中のオブジェクトの位置を検索
            otx = cmds.getAttr(SelectObj + ".translateX",time = nextframe )
            oty = cmds.getAttr(SelectObj + ".translateY",time = nextframe )
            otz = cmds.getAttr(SelectObj + ".translateZ",time = nextframe )
            #最初のフレーム位置からの距離を計測し、それをコピー先オブジェクトに入れる
            otx = otx - fotx 
            oty = oty - foty
            otz = otz - fotz
            if cmds.findKeyframe(SelectObj,at="translate",time=(nextframe-1,nextframe-1) , w="next") == nextframe:
                cmds.setAttr(CopyObj + ".translateX",fftx + otx)
                cmds.setAttr(CopyObj + ".translateY",ffty + oty)
                cmds.setAttr(CopyObj + ".translateZ",fftz + otz)
                
                cmds.setKeyframe(CopyObj,t=[nextframe,nextframe],at="translate")
           
        #キーフレーム中のオブジェクトの回転をコピー
        if rotateMode ==True:
            #キーフレーム中のオブジェクトの位置を検索
            orx = cmds.getAttr(SelectObj + ".rotateX",time = nextframe )
            ory = cmds.getAttr(SelectObj + ".rotateY",time = nextframe )
            orz = cmds.getAttr(SelectObj + ".rotateZ",time = nextframe )
            #最初のフレーム位置からの距離を計測し、それをコピー先オブジェクトに入れる
            orx = orx - forx 
            ory = ory - fory
            orz = orz - forz
            

            if cmds.findKeyframe(SelectObj,at="rotate",time=(nextframe-1,nextframe-1) , w="next") == nextframe:
                cmds.setAttr(CopyObj + ".rotateX",ffrx + orx)
                cmds.setAttr(CopyObj + ".rotateY",ffry + ory)
                cmds.setAttr(CopyObj + ".rotateZ",ffrz + orz)
            
                cmds.setKeyframe(CopyObj,t=[nextframe,nextframe],at="rotate")
            
            
        #キーフレーム中のオブジェクトの回転をコピー
        if scaleMode ==True:
            #キーフレーム中のオブジェクトの位置を検索
            osx = cmds.getAttr(SelectObj + ".scaleX",time = nextframe )
            osy = cmds.getAttr(SelectObj + ".scaleY",time = nextframe )
            osz = cmds.getAttr(SelectObj + ".scaleZ",time = nextframe )
            #最初のフレーム位置からの距離を計測し、それをコピー先オブジェクトに入れる
            osx = osx - fosx 
            osy = osy - fosy
            osz = osz - fosz
            
            if cmds.findKeyframe(SelectObj,at="scale",time=(nextframe-1,nextframe-1) , w="next") == nextframe:
                cmds.setAttr(CopyObj + ".scaleX",ffsx + osx)
                cmds.setAttr(CopyObj + ".scaleY",ffsy + osy)
                cmds.setAttr(CopyObj + ".scaleZ",ffsz + osz)

                cmds.setKeyframe(CopyObj,t=[nextframe,nextframe],at="scale")
            
        
        frame = nextframe
    cmds.currentTime(time)

