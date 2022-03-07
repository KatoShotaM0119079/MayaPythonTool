#もしウィンドウが既に存在している場合はそれを予め削除してからもう一度生成する。
WindowExists = cmds.window ("AutoCreateRig" , ex =True)
if WindowExists == True:
    cmds.deleteUI("AutoCreateRig")

#ボタン付きGUIの作成

button_window = cmds.window ("AutoCreateRig" , bgc = (0.25,0.25,0.25))
button_layout = cmds.columnLayout (adjustableColumn = True , parent = button_window )

#=====
#リグカラーの変更
#HipからHeadにかけてのテキストフィールドの配置
cmds.text(label="Change_Controller_Color",bgc = (0.15,0.15,0.15),h=25)
cmds.rowLayout( numberOfColumns=6, 
                columnWidth6=( 55, 55, 55 , 55 , 55, 55 ), 
                columnAttach=( (1,'both',0), (2,'both',0), (3,'both',0) ,(4,'both',0),(5,'both',0),(6,'both',0) )
              ) 
cmds.button(label = "" , command = ("ChangeColorToRed()") , bgc = (1,0,0),h=35)
cmds.button(label = "" , command = ("ChangeColorToYellow()"), bgc = (1,1,0),h=35)
cmds.button(label = "" , command = ("ChangeColorToGreen()"), bgc = (0,1,0),h=35)
cmds.button(label = "" , command = ("ChangeColorToCian()"), bgc = (0,1,1),h=35)
cmds.button(label = "" , command = ("ChangeColorToBlue()"), bgc = (0,0,1),h=35)
cmds.button(label = "" , command = ("ChangeColorToMasenda()"), bgc = (1,0,1),h=35)
cmds.setParent(u=True)

cmds.rowLayout( numberOfColumns=6, 
                columnWidth6=( 55, 55, 55 , 55 , 55, 55 ), 
                columnAttach=( (1,'both',0), (2,'both',0), (3,'both',0) ,(4,'both',0),(5,'both',0),(6,'both',0) )
              ) 
cmds.button(label = "" , command = ("ChangeColorToOrange()") , bgc = (1,0.75,0.25),h=35)
cmds.button(label = "" , command = ("ChangeColorToYellowGreen()"), bgc = (0.75,1,0.25),h=35)
cmds.button(label = "" , command = ("ChangeColorToEmeraldGreen()"), bgc = (0.25,1,0.75),h=35)
cmds.button(label = "" , command = ("ChangeColorToLightBlue()"), bgc = (0.25,0.75,1),h=35)
cmds.button(label = "" , command = ("ChangeColorToViolet()"), bgc = (0.75,0.25,1),h=35)
cmds.button(label = "" , command = ("ChangeColorToPink()"), bgc = (1,0.35,0.75),h=35)
cmds.setParent(u=True)

cmds.text(label="")

#======
#リグ作成ボタンの配置
cmds.text(label="Create_Rig",bgc = (0.15,0.15,0.15),h=25)
buttonD = cmds.button(label = "Create" , command = "Create()",parent=button_layout , bgc = (0.35,0.35,0.35),h=50)
#ラジオボタンの配置
cmds.rowLayout( numberOfColumns=5, 
                columnWidth5=( 90, 60 ,60 ,60 ,60 ), 
                columnAttach=( (1,'both',0), (2,'both',0), (3,'both',0), (4,'both',0), (5,'both',0) )
              ) 
collection1 = cmds.radioCollection()
rb1 = cmds.radioButton("Hips", label='Hips~Head',sl=True )
rb2 = cmds.radioButton( "Arm",label='Arm' )
rb3 = cmds.radioButton( "Leg",label='Leg' )
rb4 = cmds.radioButton( "Eye",label='Eye' )
rb5 = cmds.radioButton( "Other",label='Other')
cmds.setParent(u=True)

#ラジオボタンの配置
cmds.rowLayout( numberOfColumns=2, 
                columnWidth2=( 45, 45 ), 
                columnAttach=( (1,'both',0), (2,'both',0) )
              ) 
collection1 = cmds.radioCollection()
rb1 = cmds.radioButton("FK", label='FK',sl=True )
rb2 = cmds.radioButton("IK",label='IK' )
cmds.setParent(u=True)

cmds.text(label="")

#======
#Mirrorのボタンの配置
cmds.text(label="ControlRig_MirrorCopy",bgc = (0.15,0.15,0.15),h=25)
buttonE = cmds.button(label = "Mirror" , command = "Mirror()",parent=button_layout , bgc = (0.35,0.35,0.35),h=50)
#LegFingerのテキストフィールドの配置
cmds.rowLayout( numberOfColumns=4, 
                columnWidth4=(  50, 75 , 20 , 75 ), 
                columnAttach=( (1,'both',0), (2,'both',0),(3,'both',0),(4,'both',0) ),
                adj=True
              ) 

cmds.text(label="Replace:",h=30)
cmds.textField("ReplaceNameOrigin",h=30, tx="") 
cmds.text(label="→",h=30)
cmds.textField("ReplaceNameChange",h=30, tx="") 
cmds.setParent(u=True)

cmds.text(label="")

#======

cmds.showWindow(button_window)



#リグの作成
def Create():
    
    #ラジオボタンの状態を確認
    if cmds.radioButton("Hips", q=True ,sl=True ) == True:
        CreateMode = "Hips"
    if cmds.radioButton("Arm", q=True ,sl=True ) == True:
        CreateMode = "Arm"
    if cmds.radioButton("Leg", q=True ,sl=True ) == True:
        CreateMode = "Leg"
    if cmds.radioButton("Eye", q=True ,sl=True ) == True:
        CreateMode = "Eye"
    if cmds.radioButton("Other", q=True ,sl=True ) == True:
        CreateMode = "Other"
        
    if cmds.radioButton("FK", q=True ,sl=True ) == True:
        FKIKMode = "FK"
    if cmds.radioButton("IK", q=True ,sl=True ) == True:
        FKIKMode = "IK"
    
    #ジョイントの選択
    if FKIKMode == "FK"  and CreateMode != "Eye":
        joints = cmds.ls(sl=True,dag=True,type = "joint")
    if FKIKMode == "IK"  and CreateMode != "Eye":
        joints = cmds.ls(sl=True,type = "joint")
        startjoint = cmds.ls(joints[0],dag=True,type="joint")
    selectjoint = cmds.ls(sl=True,type = "joint")
    
    #選択しているジョイントの状態が適切かどうか調べる
    if FKIKMode == "FK" and len(selectjoint)!=1  and CreateMode != "Eye":
        cmds.error("ジョイントを1つ選択してください")
    if FKIKMode == "IK" and len(selectjoint)!=2 and CreateMode != "Eye":
        cmds.error("ジョイントを2つ選択してください")
        #IKの生成の場合、選択した二つのジョイントが、同じ階層内にあるのか調べる。無かった場合はエラー文。
        Hantei = False
        for joint in startjoint:
            if joint == joints[1]:
                Hantei = True
        if Hantei != True:
            cmds.error("同じ階層内のジョイントを選択してください。")
        

    #リグを作成するジョイントのリストを作成
    #FKの場合
    if CreateMode == "Hips":
        jointList = []
        if joints[0].find("Hips") == -1:
            cmds.error("Hipsジョイントを選択してください")
        for joint in joints:
            if joint[:4].find("Left") == -1 and joint[:5].find("Right") == -1 :
                jointList.append(joint)
                
    if CreateMode == "Arm":
        if joints[0].find("Shoulder") == -1 and joints[0].find("Arm") == -1:
            cmds.error("ArmかShoulderジョイントを選択してください")
        if joints[0].find("Shoulder") != 0 or joints[0].find("Arm") != 0:
            jointList = []
            for joint in joints:
                jointList.append(joint)

    if CreateMode == "Leg":
        if joints[0].find("Leg") == -1 :
            cmds.error("Legジョイントを選択してください")
        if joints[0].find("Leg") != 0 :
            jointList = []
            for joint in joints:
                jointList.append(joint)       
                
    if FKIKMode == "FK" and CreateMode == "Other":
       jointList = []
       for joint in joints:
            jointList.append(joint)  
            
    #FKの場合のリグの作成   
    if FKIKMode == "FK"  and CreateMode != "Eye":
        for joint in jointList:
            #もしコントローラが既に存在していた場合は削除しておく
            if cmds.objExists(str(joint) + "_Ctrl") == True:
                cmds.delete(str(joint) + "_Ctrl")
            
            #コントローラの生成
            if CreateMode == "Hips" or CreateMode == "Leg" or CreateMode == "Other":            
                cmds.circle(nry=90 ,r=15 , n=str(joint) + "_Ctrl")
            if CreateMode == "Arm" :            
                cmds.circle(nrx=90 ,r=15 , n=str(joint) + "_Ctrl")
            Circle = str(joint) + "_Ctrl"
            
            pc = cmds.pointConstraint(joint,Circle)
            cmds.delete(pc)
            
            #もしコンストレイントが既に存在していた場合は削除しておく
            if cmds.objExists(str(joint)+"_orientConstraint1") == True:
                cmds.delete(str(joint)+"_orientConstraint1")
            
            #コンストレイントの設定
            cmds.orientConstraint(Circle,joint,mo=True)
            
            
            #ヒストリの削除とトランスフォームのフリーズ
            mel.eval("FreezeTransformations")
            mel.eval("DeleteHistory")
            
            #階層の作成
            if joint != jointList[0]:
                cmds.parent(Circle,Ctrl)
            Ctrl = Circle
            
            #一番上のコントローラは不要のため削除
            if joint == jointList[len(jointList)-1]:
                cmds.delete(Circle)
              
        if len(joints) > 0:
            parentjoint = cmds.listRelatives(selectjoint[0],p=True) 
            parentjoint = str(parentjoint).replace("['","")
            parentjoint = str(parentjoint).replace("']","")
            if cmds.objExists (str(parentjoint) + "_Ctrl"):
                parentCtrl = str(parentjoint) + "_Ctrl"
                cmds.parent(str(joints[0])+"_Ctrl" , parentCtrl ) 
            cmds.select(str(joints[0])+"_Ctrl")
            
    #IKの場合のリグの作成
    if FKIKMode == "IK" and CreateMode != "Eye":    
        IK = cmds.ikHandle(sj=joints[0],ee=joints[1],n=str(joints[1]+"_IK"))
        
        #もしコントローラが既に存在していた場合は削除しておく
        if cmds.objExists(str(joints[1]) + "_Ctrl_IK") == True:
            cmds.delete(str(joints[1]) + "_Ctrl_IK")
        
        #コントローラの生成
        if CreateMode == "Hips" or CreateMode == "Leg" or CreateMode == "Other":            
            cmds.circle(nry=90 ,r=15 , n=str(joints[1]) + "_Ctrl_IK" , d=1 , s=4)
            Circle = str(joints[1]) + "_Ctrl_IK"
            cmds.setAttr(Circle + ".rotateY" , 45)
        if CreateMode == "Arm" :            
            cmds.circle(nrx=90,nry=0 ,r=15 , n=str(joints[1]) + "_Ctrl_IK" , d=1 , s=4)
            Circle = str(joints[1]) + "_Ctrl_IK"
            cmds.setAttr(Circle + ".rotateX" , 45)
        
        
        pc = cmds.pointConstraint(joints[1],Circle)
        cmds.delete(pc)
        
        
        #ヒストリの削除とトランスフォームのフリーズ
        mel.eval("FreezeTransformations")
        mel.eval("DeleteHistory")
        
        #コンストレイントの設定
        cmds.pointConstraint(Circle,IK[0],mo=True)
        
        #PoleVeltorの自動設定
        parentjoint = cmds.listRelatives(joints[1],ap=True ) 
        parentjoint = str(parentjoint).replace("['","")
        parentjoint = str(parentjoint).replace("']","")
        
        if parentjoint != joints[0]:
            joint = cmds.listRelatives(joints[1],p=True)
            
            #PoleVector用のロケーターの生成
            cmds.spaceLocator( n = str(joint[0]) + "_Loc" , p=(0, 0, 0) )
            Locator =  str(joint[0]) + "_Loc"
            cmds.setAttr(Locator + ".localScaleX" , 5)
            cmds.setAttr(Locator + ".localScaleY" , 5)
            cmds.setAttr(Locator + ".localScaleZ" , 5)
            
            pc = cmds.pointConstraint(joint,Locator)
            cmds.delete(pc)
            
            if CreateMode == "Leg" or CreateMode == "Other":  
                cmds.setAttr(Locator + ".translateZ" , cmds.getAttr(Locator + ".translateZ") + 30)
            if CreateMode == "Arm" or CreateMode == "Hips":  
                cmds.setAttr(Locator + ".translateZ" , cmds.getAttr(Locator + ".translateZ") + -30)
            
            #ヒストリの削除とトランスフォームのフリーズ
            mel.eval("FreezeTransformations")
            mel.eval("DeleteHistory")
        
            cmds.poleVectorConstraint(Locator,IK[0],n= str(joint) + "_PoleVector")
      
    #目のエイム設定  
    if CreateMode == "Eye":
        joints = cmds.ls(sl=True,type="joint")
        if len(joints) > 2 or len(joints) < 1:
            cmde.error("ジョイントを1つか2つ選択してください")
        
        #二つ選択している場合、ジョイントがX軸の+と-にあるか判定し、もし判定された場合は両目用のロケータを作成
        EyesHantei = False
        if len(joints) == 2:
            if cmds.getAttr(joints[0] + ".translateX") > 0 and cmds.getAttr(joints[1] + ".translateX") < 0:
                EyesHantei = True
            if cmds.getAttr(joints[0] + ".translateX") < 0 and cmds.getAttr(joints[1] + ".translateX") > 0:
                EyesHantei = True
        
        #ジョイント1に対する設定
        cmds.circle(nrz=90 ,r=5 , n = str(joints[0]) + "_Loc")
        Loc0 = str(joints[0]) + "_Loc"
        pc = cmds.pointConstraint(joints[0],Loc0)
        cmds.delete(pc)
        cmds.setAttr(Loc0 + ".translateZ",cmds.getAttr(Loc0 + ".translateZ")+30 )
        if cmds.getAttr(Loc0 + ".translateX") > 0 and EyesHantei == True:
            cmds.setAttr(Loc0 + ".translateX" , 10)
        elif cmds.getAttr(Loc0 + ".translateX") < 0 and EyesHantei == True:
            cmds.setAttr(Loc0 + ".translateX" , -10)
        
        #ヒストリの削除とトランスフォームのフリーズ
        mel.eval("FreezeTransformations")
        mel.eval("DeleteHistory")
        
        #エイムコンストレイント設定
        cmds.aimConstraint(Loc0,joints[0],mo=True,n=joints[0]+"_Aim",aim=(0,0,1),u=(0,1,0),wu=(0,1,0))
        
        Circle = Loc0
        
        #ジョイント2に対する設定
        if len(joints) ==2:    
            cmds.circle(nrz=90 ,r=5 , n = str(joints[1]) + "_Loc")
            Loc1 =  str(joints[1]) + "_Loc"
            pc = cmds.pointConstraint(joints[1],Loc1)
            cmds.delete(pc)
            cmds.setAttr(Loc1 + ".translateZ",cmds.getAttr(Loc1 + ".translateZ")+30 )
            if cmds.getAttr(Loc1 + ".translateX") > 0 and EyesHantei == True:
                cmds.setAttr(Loc1 + ".translateX" , 10)
            elif cmds.getAttr(Loc1 + ".translateX") < 0 and EyesHantei == True:
                cmds.setAttr(Loc1 + ".translateX" , -10)
                        
            #ヒストリの削除とトランスフォームのフリーズ
            mel.eval("FreezeTransformations")
            mel.eval("DeleteHistory")
            
            #エイムコンストレイント設定
            cmds.aimConstraint(Loc1,joints[1],mo=True,n=joints[1]+"_Aim",aim=(0,0,1),u=(0,1,0),wu=(0,1,0))
            
            Circle = Loc1
            
        #両目を制御するための設定
        if len(joints) ==2:
            cmds.circle(nrz=90 ,r=7.5 , n="Eyes" + "_Loc" , d=1 , s=4)
            Loc = "Eyes" + "_Loc"
            cmds.setAttr(Loc + ".rotateZ" , 45)
            
            #ヒストリの削除とトランスフォームのフリーズ
            mel.eval("FreezeTransformations")
            mel.eval("DeleteHistory")
            
            cmds.setAttr(Loc + ".scaleX" , 3)
            mel.eval("FreezeTransformations")
                        
            #両目のロケータの中心位置にロケータを設置
            L0 = cmds.spaceLocator( n =  "pointPositionLoc0" , p=(0, 0, 0) )
            L1 = cmds.spaceLocator( n =  "pointPositionLoc1" , p=(0, 0, 0) )
            pc = cmds.pointConstraint(Loc0,L0)
            cmds.delete(pc)
            pc = cmds.pointConstraint(Loc1,L1)
            cmds.delete(pc)
            
            Lt0 = cmds.pointPosition(L0)
            Lt1 = cmds.pointPosition(L1)
            
            cmds.delete(L0)
            cmds.delete(L1)
            
            tx = (Lt0[0] + Lt1[0])/2 
            ty = (Lt0[1] + Lt1[1])/2 
            tz = (Lt0[2] + Lt1[2])/2
            
            cmds.setAttr(Loc + ".translateX" , tx)
            cmds.setAttr(Loc + ".translateY" , ty)
            cmds.setAttr(Loc + ".translateZ" , tz)
            
            cmds.parent(Loc0,Loc)
            cmds.parent(Loc1,Loc)
            cmds.select(Loc)
            #ヒストリの削除とトランスフォームのフリーズ
            mel.eval("FreezeTransformations")
            mel.eval("DeleteHistory")    
            Circle = Loc
        
        cmds.select(Circle)
    
    
#リグミラーの作成
def Mirror():
    Ctrls = cmds.ls(sl=True,type = "transform")
    if len(Ctrls) != 1:
        cmds.error("コントローラを一つ選択してください")
    
    if cmds.textField("ReplaceNameOrigin",q=True,text=True) == "" or cmds.textField("ReplaceNameChange",q=True,text=True) == "":
        cmds.error("ミラー後に変更する名前を設定してください")
        
    replaceNameOrigin = cmds.textField("ReplaceNameOrigin",q=True,text=True)
    replaceNameChange = cmds.textField("ReplaceNameChange",q=True,text=True)
            
    Ctrls = cmds.ls(sl=True,dag=True,type = "transform")
    
    if len(Ctrls) > 0:
        duplicateCtrls = cmds.duplicate(Ctrls[0],rc=True)
        Group = cmds.group(duplicateCtrls[0],n="MirrorGroup",r=True)

        
        cmds.move(0, 0, 0, Group + '.scalePivot', Group + '.rotatePivot', rpr=1)
        cmds.setAttr(Group+".scaleX",-1)        
        cmds.ungroup(Group)
        
        mel.eval("FreezeTransformations")
        mel.eval("DeleteHistory")
        
        num = 0
        selCtrl = ""
        for Ctrl in Ctrls:
            #名前の変更
            CtrlName = duplicateCtrls[num]
            if Ctrl.find(replaceNameOrigin) != -1:
                originCtrl = Ctrl
                CtrlName = Ctrl.replace(replaceNameOrigin,replaceNameChange) 
                CtrlName = cmds.rename(duplicateCtrls[num],CtrlName)
                if selCtrl == "":
                    selCtrl = CtrlName
            
            
            #コンストレイントの検索と自動設定
            PoleVectroHantei = False
            if CtrlName.find("_Ctrl_IK") != -1:
                joint = CtrlName.replace("_Ctrl_IK","")
                startjoint = cmds.ikHandle( originCtrl.replace("_Ctrl","") ,q=True ,sj=True) 
                startjoint = startjoint.replace(replaceNameOrigin,replaceNameChange)
                IK = cmds.ikHandle(sj=startjoint,ee=CtrlName.replace("_Ctrl_IK",""),n=str(joint+"_IK"))
                IK = str(joint+"_IK")
                PoleVectroHantei = True
            
            if cmds.objExists(Ctrl.replace("_Ctrl","")+"_orientConstraint1"):
                joint = CtrlName.replace("_Ctrl","")
                cmds.orientConstraint(CtrlName,joint,mo=1)
                
            if cmds.objExists(Ctrl.replace("_Ctrl","")+"_pointConstraint1"):
                joint = CtrlName.replace("_Ctrl","")
                cmds.pointConstraint(CtrlName,joint,mo=1)
                
            if cmds.objExists(Ctrl.replace("_Ctrl","")+"_parentConstraint1"):
                joint = CtrlName.replace("_Ctrl","")
                cmds.parentConstraint(CtrlName,joint,mo=1)
                
            if PoleVectroHantei == True:
                joint = cmds.listRelatives(Ctrl.replace("_Ctrl_IK",""),p=True)
                joint = str(joint).replace("['","")
                joint = str(joint).replace("']","")
                Loc = str(joint) + "_Loc"
                #ここから書く　ポールベクター用ロケータを見つけた後、コピーして名前を変更　コンストレイントを行う
                if cmds.objExists(Loc):
                    originLoc = Loc
                    Loc = Loc.replace(replaceNameOrigin,replaceNameChange)
                    duplicateLoc = cmds.duplicate(originLoc,rc=True)
                    LocGroup = cmds.group(duplicateLoc,n="MirrorLoC",r=True)
                    cmds.move(0, 0, 0, LocGroup + '.scalePivot', LocGroup + '.rotatePivot', rpr=1)
                    cmds.setAttr(LocGroup+".scaleX",-1)
                    cmds.ungroup(LocGroup)
                    
                    mel.eval("FreezeTransformations")
                    mel.eval("DeleteHistory")
                    
                    Loc = cmds.rename(duplicateLoc,Loc)
                    cmds.poleVectorConstraint(Loc,IK ,n= str(startjoint) + "_PoleVector")

            num = num + 1
        cmds.select(selCtrl)
    
    
#リグカラーの変更
def ChangeColorToRed():    
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)

        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",1)
        cmds.setAttr(Ctrl + ".overrideColorG",0)
        cmds.setAttr(Ctrl + ".overrideColorB",0)
        
def ChangeColorToYellow():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",1)
        cmds.setAttr(Ctrl + ".overrideColorG",1)
        cmds.setAttr(Ctrl + ".overrideColorB",0)
        
def ChangeColorToGreen():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0)
        cmds.setAttr(Ctrl + ".overrideColorG",1)
        cmds.setAttr(Ctrl + ".overrideColorB",0)
        
def ChangeColorToCian():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0)
        cmds.setAttr(Ctrl + ".overrideColorG",1)
        cmds.setAttr(Ctrl + ".overrideColorB",1)
    
def ChangeColorToBlue():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0)
        cmds.setAttr(Ctrl + ".overrideColorG",0)
        cmds.setAttr(Ctrl + ".overrideColorB",1)
            
def ChangeColorToMasenda():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",1)
        cmds.setAttr(Ctrl + ".overrideColorG",0)
        cmds.setAttr(Ctrl + ".overrideColorB",1)
        
def ChangeColorToOrange():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",1)
        cmds.setAttr(Ctrl + ".overrideColorG",0.75)
        cmds.setAttr(Ctrl + ".overrideColorB",0.25)
        
def ChangeColorToYellowGreen():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0.75)
        cmds.setAttr(Ctrl + ".overrideColorG",1)
        cmds.setAttr(Ctrl + ".overrideColorB",0.25)
    
def ChangeColorToEmeraldGreen():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0.25)
        cmds.setAttr(Ctrl + ".overrideColorG",1)
        cmds.setAttr(Ctrl + ".overrideColorB",0.5)    
        
def ChangeColorToLightBlue():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0.25)
        cmds.setAttr(Ctrl + ".overrideColorG",0.75)
        cmds.setAttr(Ctrl + ".overrideColorB",1)
        
def ChangeColorToViolet():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",0.5)
        cmds.setAttr(Ctrl + ".overrideColorG",0)
        cmds.setAttr(Ctrl + ".overrideColorB",1)    

def ChangeColorToPink():
    Ctrls = cmds.ls(sl=True,dag=True,type="nurbsCurve")
    
    for Ctrl in Ctrls:
        cmds.setAttr(Ctrl + ".overrideEnabled",1)
    
        cmds.setAttr(Ctrl + ".overrideRGBColors",1)
        
        #RGB各色を設定
        cmds.setAttr(Ctrl + ".overrideColorR",1)
        cmds.setAttr(Ctrl + ".overrideColorG",0.35)
        cmds.setAttr(Ctrl + ".overrideColorB",0.75) 