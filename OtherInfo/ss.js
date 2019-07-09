var _template = [
        '<ul class="nav navbar-nav navbar-left nav-system">',
        '  <li class="dropdown">',
        '    <a href="javascript:;" class="dropdown-toggle" data-toggle="dropdown" title="切换系统">',
        '     {{curSystemName}} {{#multiple}}<i class="fa fa-caret-down"></i>{{/multiple}}',
        '    </a>',
        '    {{#multiple}}<ul class="dropdown-menu">',
        '        {{#systems}}',
        '           {{^first}}<li role="separator" class="divider"></li>{{/first}}',
        '           <li>',
        '               <a href="{{{systemHttpUrl}}}" target="_self">{{systemName}}</a>',
        '           </li>',
        '        {{/systems}}',
        '    </ul>{{/multiple}}',
        '  </li>',
        '</ul>'
    ].join('');

//初始化这个模板
Mustache.parse(_template);
function data2Html(data) {
    data = data || [];
    var curSysAry = data.filter(function(s){ 
    data.sort(function(a, b){ return a.sortOrder - b.sortOrder;});
    data = data.map(function(s, i){s.first = i == 0; return s});

    //模板渲染成字符串
    return Mustache.render(_template, {
        curSystemName: curSysAry.length ? curSysAry[0].systemName : '',
        multiple: !!data.length,
        systems: data
    });
}