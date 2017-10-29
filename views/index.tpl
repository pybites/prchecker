% include('header.tpl', title='Page Title')

  <h2>This Month's Open Pull Requests for <a href="https://pybit.es/pages/challenges.html">PyBites Code Challenges</a></h2>
  % if prs:

    <table id="prs" class="mui-table">
      <thead>
        <tr>
          <th>User</th>
          <th>Title</th>
          <th>Body</th>
          <th>Created</th>
        </tr>
      </thead>
      <tbody>
        % for pr in prs:
          <tr>
            <td><a href="users/{{ pr.user.name }}"><img src="{{ pr.user.avatar_url }}"></a></td>
            <td><a href="{{ pr.url }}" target="_blank">{{ pr.title }}</a></td>
            <td><pre>{{ pr.feedback }}</pre></td>
            <td>{{ pr.created }}</td>
          </tr>
        % end
      </tbody>
    </table>

  % else:

    <h2>No Prs submitted yet</h2>
    <p>Or better said: <a href="https://pybit.es/pages/challenges.html">time to get coding</a>!</p>
  % end

% include('footer.tpl')
