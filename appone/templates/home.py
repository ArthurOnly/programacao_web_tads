{% if users %}
    <ul>
    {% for user in users %}
        <li><a href="/polls/{{ user.id }}/">{{ user.name }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No users are available.</p>
{% endif %}