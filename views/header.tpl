<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.muicss.com/mui-latest/css/mui.min.css" rel="stylesheet" type="text/css" />
    <link href="static/css/style.css" rel="stylesheet" type="text/css" />
    <script src="//cdn.muicss.com/mui-latest/js/mui.min.js"></script>
    <title>PyBites PR checker</title>
  </head>
  <body>
    <header class="mui-appbar mui--z1">
      <div class="mui-container">
        <table width="100%">
          <tr class="mui--appbar-height">
            <td class="mui--text-title">
              <a href="https://pybit.es/">
                <img id="logo" src='https://avatars0.githubusercontent.com/u/24620154?s=400&v=4' alt='PyBites'></a>
            </td>

            <td class="mui--text-title">
              <form action="/" class="mui-form--inline" method="POST">
                <div class="mui-textfield">
                  <input name="username" type="text" placeholder="Github username">
                </div>
                <button type="submit" class="mui-btn mui-btn--raised">Check PRs</button>
              </form>
            </td>

            <td align="right">
              <ul class="mui-list--inline mui--text-body2">
                <li><a href="/">Home</a></li>
                <li><a href="https://pybit.es/codechallenge38.html">Challenge</a></li>
              </ul>
            </td>
          </tr>
        </table>
      </div>
    </header>
