import fitz, json, re, os, sys
SRC='../official-practice-tests'
FILES={n:f'sat-practice-test-{n}.pdf' for n in [4,5,6,7,8,10,11]}; FILES[9]='   wq.pdf'
SECS=[('rw1',33),('rw2',33),('m1',27),('m2',27)]
os.makedirs('img',exist_ok=True)
def boxes(p):
    W=p.rect.width; out=[]
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            t=''.join(s['text'] for s in l['spans']).strip(); s0=l['spans'][0]
            if t.isdigit() and s0['color']==16777215 and 8<s0['size']<13 and 80<l['bbox'][1]<735:
                out.append((int(t),fitz.Rect(l['bbox'])+(-8,-2,0,0)))
    # unnumbered standard boxes (digit missing from text layer)
    for dr in p.get_drawings():
        r=dr['rect']; f=dr.get('fill')
        if f and max(f)<0.2 and 16<r.width<20 and 10<r.height<14 and 80<r.y0<735 and (abs(r.x0-36)<6 or abs(r.x0-W/2-8)<8):
            if not any(abs(o[1].y0-r.y0)<8 and (o[1].x0>W/2)==(r.x0>W/2) for o in out): out.append((None,r))
    return out
def key(n):
    a=fitz.open(f'{SRC}/scoring-practice-test-{n}.pdf')
    t=next(a[i].get_text() for i in range(len(a)) if 'Answer Key' in a[i].get_text() and 'QUESTION' in a[i].get_text())
    t=t[t.index('Answer Key'):]
    L=[x.strip() for x in t.split('\n') if x.strip()]
    secs=[[]]
    for i,x in enumerate(L):
        cur=secs[-1]; exp=len(cur)+1
        m=re.match(r'^(\d+)\s+(\S.*)$',x)
        if m and int(m[1]) in (exp,1) and re.fullmatch(r'[-\d./; ]+',m[2]): q,ans=int(m[1]),m[2]
        elif x.isdigit() and i+1<len(L) and int(x) in (exp,1) and re.fullmatch(r'[A-D]|[-\d./; ]+',L[i+1]) and not re.match(r'^\d+\s',L[i+1]): q,ans=int(x),L[i+1]
        else: continue
        if q==1 and len(cur)>=20: secs.append([]); cur=secs[-1]
        if q==len(cur)+1: cur.append(ans)
    secs=[x for x in secs if len(x)>=20]
    for i in range(len(secs)-3):
        if [len(x) for x in secs[i:i+4]]==[33,33,27,27]: return secs[i:i+4]
    return [[],[],[],[]]
def expl(n):
    t=''.join(p.get_text() for p in fitz.open(f'{SRC}/answer-explanations-practice-test-{n}.pdf'))
    parts=re.split(r'QUESTION\s+(\d+)\s*\n',t)
    secs=[];out=[]
    for i in range(1,len(parts),2):
        q=int(parts[i]);b=parts[i+1]
        if q==1: secs.append([])
        m=re.search(r'Choice\s+([A-D])\s+is\s+(?:the best answer|correct)',b)
        g=re.search(r'correct answer is\s+(.{1,40}?)\.\s',b.replace('\n',' '))
        a=m[1] if m else (re.sub(r'\s+','',g[1]) if g else '?')
        body=b.split('QUESTION')[0].strip()
        if secs: secs[-1].append((a,body[:3000]))
    return secs
data={}
for n,fn in sorted(FILES.items()):
    d=fitz.open(f'{SRC}/{fn}'); qs=[]; si=-1; last=99
    for pn,p in enumerate(d):
        W=p.rect.width
        bx=sorted(boxes(p),key=lambda b:(b[1].x0>W/2,b[1].y0))
        for i,(q,r) in enumerate(bx):
            if q is None:
                j=next((j for j in range(i+1,len(bx)) if bx[j][0] is not None),None)
                if j is not None: bx[i]=(bx[j][0]-(j-i),r)
        for k,(q,r) in enumerate(bx):
            if q is None: q=last+1 if last<99 else 1
            if q<last-5: si+=1
            last=q
            if si>3: break
            right=r.x0>W/2
            nxt=[b[1].y0 for b in bx if (b[1].x0>W/2)==right and b[1].y0>r.y0+5]
            y1=min(nxt)-6 if nxt else p.rect.height-48
            x0,x1=(W/2+2,W-28) if right else (28,W/2-2)
            name=f'img/t{n}_{SECS[si][0]}_{q}.png'
            p.get_pixmap(clip=fitz.Rect(x0,r.y0-4,x1,y1),dpi=170,colorspace=fitz.csGRAY).save(name)
            qs.append((SECS[si][0],q,name))
    ks=key(n); ex=expl(n); test={}
    for i in range(4):
        e=ex[i] if i<len(ex) else []
        mc=[(k,x[0]) for k,x in zip(ks[i],e) if len(k)==1 and len(x[0])==1]
        bad=sum(k!=x for k,x in mc)
        if bad>0 or len(ks[i])!=len(e):
            print('  key mismatch',n,SECS[i][0],bad,'-> using explanations'); ks[i]=[x[0] for x in e]
    for i,(s,cnt) in enumerate(SECS):
        items=sorted([x for x in qs if x[0]==s],key=lambda x:x[1])
        test[s]=[{'n':q,'img':im,'ans':(ks[i][q-1] if q-1<len(ks[i]) else '?'),'ex':(ex[i][q-1][1] if i<len(ex) and q-1<len(ex[i]) else '')} for _,q,im in items]
        nums=[x['n'] for x in test[s]]
        flag='' if nums==list(range(1,cnt+1)) and len(ks[i])==cnt else f'  !! got {len(nums)} missing {sorted(set(range(1,cnt+1))-set(nums))} key {len(ks[i]) if i<len(ks) else 0}'
        print(n,s,len(nums),flag)
    data[n]=test
open('data.js','w').write('window.DATA='+json.dumps(data)+';')
OVR={('4','m2',6):'15; -5'}
for (t,sec,qn),v in OVR.items(): data[int(t)][sec][qn-1]['ans']=v
# clean grid-in answers from the "Note that X and Y are examples" line
for t in data.values():
    for qs_ in t.values():
        for q in qs_:
            if len(q['ans'])==1: continue
            m=re.search(r'Note that (.+?) (?:is an example|are examples)',q['ex'].replace('\n',' '))
            if m and len(q['ans'].split(';'))<2:
                q['ans']='; '.join(x.strip() for x in re.split(r',\s*(?:and\s+)?|\s+and\s+',m[1]) if x.strip())
open('data.js','w').write('window.DATA='+json.dumps(data)+';')
from PIL import Image, ImageOps
import glob
for f in glob.glob('img/*.png'):
    im=Image.open(f); bb=ImageOps.invert(im.convert('L')).point(lambda v:255 if v>30 else 0).getbbox()
    if bb: im.crop((0,0,im.width,min(im.height,bb[3]+20))).save(f,optimize=True)
# ---- explanation crops (exact PDF look) ----
os.makedirs('exp',exist_ok=True)
def expcrops(n):
    d=fitz.open(f'{SRC}/answer-explanations-practice-test-{n}.pdf'); heads=[]
    for pn,p in enumerate(d):
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                t=''.join(s['text'] for s in l['spans']).strip()
                m=re.fullmatch(r'QUESTION\s+(\d+)',t)
                if m: heads.append((pn,l['bbox'][1],int(m[1])))
    si=-1; res={}
    for k,(pn,y,q) in enumerate(heads):
        if q==1: si+=1
        if si>3: break
        end=heads[k+1][:2] if k+1<len(heads) else (len(d)-1,735)
        parts=[];cp,cy=pn,y-4
        while True:
            last=(cp==end[0]); y1=end[1]-6 if last else 735
            if y1-cy>12:
                clip=fitz.Rect(45,cy,570,y1); name=f'exp/t{n}_{SECS[si][0]}_{q}_{len(parts)}.png'
                d[cp].get_pixmap(clip=clip,dpi=130,colorspace=fitz.csGRAY).save(name); parts.append(name)
            if last or cp-pn>2: break
            cp+=1; cy=68
        res[(SECS[si][0],q)]=parts
    return res
for n in data:
    ec=expcrops(n)
    for s,qs_ in data[n].items():
        for q in qs_: q['exi']=ec.get((s,q['n']),[]); q.pop('ex',None) if q['exi'] else None
    print('exp',n,sum(len(v)>0 for v in ec.values()))
for f in glob.glob('exp/*.png'):
    im=Image.open(f); bb=ImageOps.invert(im.convert('L')).point(lambda v:255 if v>30 else 0).getbbox()
    if bb: im.crop((0,0,im.width,min(im.height,bb[3]+14))).save(f,optimize=True)
    else: os.remove(f)
for t in data.values():
    for qs_ in t.values():
        for q in qs_:
            if 'exi' in q: q['exi']=[f for f in q['exi'] if os.path.exists(f)]
open('data.js','w').write('window.DATA='+json.dumps(data)+';')
