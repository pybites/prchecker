% include('header.tpl')

<div id="content-wrapper" class="mui--text-center">
  <div class="mui--appbar-height"></div>

  <br><br>

  <h2>
    % if header:
      {{ header }}
    % else:
      This Month's Open Pull Requests for <a href="https://pybit.es/pages/challenges.html">PyBites Code Challenges</a>
    % end
  </h2>


  % if prs:

    <table id="prs" class="mui-table mui-table--bordered">
      <thead>
        <tr>
          <th>User</th>
          <th>Title</th>
          <th>Created</th>
          <th>PR description</th>
        </tr>
      </thead>
      <tbody>
        % for pr in prs:
          <tr>
            <td><a href="/{{ pr.user.login }}"><img src="{{ pr.user.avatar_url }}"></a></td>
            <td><a href="{{ pr.url }}" target="_blank">{{ pr.title }}</a></td>
            <td>{{ pr.created }}</td>
            <td>{{ pr.feedback }}</td>
          </tr>
        % end
      </tbody>
    </table>

  % else:

    <h2>No Prs submitted yet</h2>
    <p>Or better said: <a href="https://pybit.es/pages/challenges.html">time to get coding</a>!</p>

  % end

  </div>

% include('footer.tpl')
