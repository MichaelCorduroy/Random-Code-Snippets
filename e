<h1>SPAGETT</h1>
<p id = "scoreLable"></p>
<canvas id="gc" width="400" height="400"></canvas>
<h1>Credits:</h1>
<h4> Michael Azubike</h4>

<p id = "score"> </p>
<script>
	var score = 0;
window.onload=function() {
    canv=document.getElementById("gc");
    ctx=canv.getContext("2d");
    document.addEventListener("keydown",keyPush);
    setInterval(game,1000/15);
}
px=py=10;
gs=tc=20;
ax=ay=15;
xv=yv=0;
trail=[];
tail = 1;
function game() {
    px+=xv;
    py+=yv;
    if(px<0) {
        px= tc-1;
    }
    if(px>tc-1) {
        px= 0;
    }
    if(py<0) {
        py= tc-1;
    }
    if(py>tc-1) {
        py= 0;
    }
    ctx.fillStyle="orange";
    ctx.fillRect(0,0,canv.width,canv.height);
 
    ctx.fillStyle="white";
    for(var i=0;i<trail.length;i++) {
        ctx.fillRect(trail[i].x*gs,trail[i].y*gs,gs-2,gs-2);
        if(trail[i].x==px && trail[i].y==py) {
            tail = 5;
        }
    }
    trail.push({x:px,y:py});
    while(trail.length>tail) {
    trail.shift();
    }


    if(ax==px && ay==py) {
        tail++;
        ax=Math.floor(Math.random()*tc);
        ay=Math.floor(Math.random()*tc);
        score++;
       
    }
    ctx.fillStyle="blue";
    ctx.fillRect(ax*gs,ay*gs,gs-2,gs-2);
}
function keyPush(evt) {
    switch(evt.keyCode) {
        case 65:
            xv=-1;yv=0;
            break;
        case 87:
            xv=0;yv=-1;
            break;
        case 68:
            xv=1;yv=0;
            break;
        case 83:
            xv=0;yv=1;
            break;
    }
}



/*
<h4>Alex Seman</h4>
<h4>Dominic Savarino - descendant of mussolinis aka only bad guy from italy</h4>
<h4>Ben Leebron - great guy - bad at snake but tries his best</h4>
<h4>Michael Sharcidzuh</h4>
<h4>Van Bran cereal - had idea for mobile version</h4>

*/
</script>
