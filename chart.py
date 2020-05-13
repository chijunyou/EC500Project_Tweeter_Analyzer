import pandas as pd
import numpy as np
html_modle="""
<br><b>{title}</b><br>
<table border="1px" style="table-layout:fixed >
<tbody border="1px" width="100px" height="200px" >
              <!--<td height =""  cellspacing="0" class="perc_filled"  bgcolor="" align="center"> </td> -->
        {histogramTdHtml}
    <tr>
               <!--<td  style="word-break:break-all;" align="center" ></td> -->
    {labHtml}
    </tr>
</tbody>
</table>
"""
 
histogramTdHtmlTempletNonzero="""
    <td>
        <table  width="100px" height="200px">
            <tbody>
             <tr>
              <td  height =""  cellspacing="0" class="perc_filled"  bgcolor="" align="center"></td>
             </tr>
             <tr>
              <td  height ="{percent}" cellspacing="0" class="perc_filled"  bgcolor="{color}" align="center">{percentText}</td>
             </tr>
            </tbody>
        </table>
    </td>
"""
 
histogramTdHtmlTempletZero="""
    <td>
        <table  width="100px" height="200px">
            <tbody>
             
            </tbody>
        </table>
    </td>
"""
 
labHtmlTemplet="""
            <td  style="word-break:break-all;" align="center" >{lable}</td>
"""

def DataFrame2HistogramHtml(title,df):
    pd.DataFrame()
    histogramTdHtml=""
    labHtml=""
    for i  in range(0,len(df)):
        lable=df.loc[i][0]
        percent=df.loc[i][1]
        percentText=percent
        percentData=int(percent.replace("%",""))

        labHtml=labHtml+labHtmlTemplet.format(lable=lable)
        color="#0099FF"
        

        if(percentData>30):
            color="#FF0000"
        elif(percentData>10):
            color="#FFCC00"
            
        

        if(percentData==0):
            #print(percent)
            histogramTdHtmlTemplet=histogramTdHtmlTempletZero
            percentText=""
        elif(percentData<10):
            histogramTdHtmlTemplet=histogramTdHtmlTempletNonzero
            percentText=""
        else:
            histogramTdHtmlTemplet=histogramTdHtmlTempletNonzero
            
        histogramTdHtml=histogramTdHtml+histogramTdHtmlTemplet.format(percent=percent,color=color,percentText=percentText)
        
    #print(histogramTdHtml)
    #print(labHtml)
    html=html_modle.format(title=title,histogramTdHtml=histogramTdHtml,labHtml=labHtml)
    #print(html)
    return html
    
    
def savechar(data,path = "templates/chart.html"):
    s1=pd.Series(np.array(["-5","-4","-3","-2","-1","0","1","2","3","4","5"]))
    s2=pd.Series(np.array(data))
    df=pd.DataFrame({"m":s1,"u":s2});
    html=DataFrame2HistogramHtml("Sentimental Analyze",df)
    f=open(path,"w")

    f.write(html)
    f.close

if __name__=='__main__':
    #RESULT_STR=''
    savechar(["-5","-4","-3","-2","-1","0","1","2","3","4","5"])
