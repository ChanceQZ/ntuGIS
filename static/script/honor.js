var timer1 = null,
    index1 = 0,
    pics1 = byId("banner1").getElementsByTagName("div"),
    dots1 = byId("dots1").getElementsByTagName("span"),
    size1 = pics1.length

function byId1(id){
  return typeof(id)==="string"?document.getElementById(id):id;
}

// 清除定时器,停止自动播放
function stopAutoPlay1(){
  if(timer1){
       clearInterval(timer1);
  }
}

// 图片自动轮播
function startAutoPlay1(){
   timer1 = setInterval(function(){
       index1++;
       if(index1 >= size1){
          index1 = 0;
       }
       changeImg1();
   },3000)
}

function changeImg1(){
   for(var i=0,len=dots1.length;i<len;i++){
       dots1[i].className = "";
       pics1[i].style.display = "none";
   }
   dots1[index1].className = "active";
   pics1[index1].style.display = "block";
}

function slideImg1(){
    var main = byId1("honor");
    var banner = byId1("banner1");
    var menuContent = byId1("menu-content");
    main.onmouseover = function(){
      stopAutoPlay1();
    }
    main.onmouseout = function(){
      startAutoPlay1();
    }
    main.onmouseout();

    // 点击导航切换
    for(var i=0,len=dots1.length;i<len;i++){
       dots1[i].id = i;
       dots1[i].onclick = function(){
           index1 = this.id;
           changeImg1();
       }
    }
}

slideImg1();