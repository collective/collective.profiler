Introduction
============

``collective.profiler`` is a tool that helps developers to analyze code
performance.  

To use it, declare the methods that you want to profile using ZCML
directives. These methods will be patched to enable profiling. 

It uses the excellent **profilehooks** package. ``collective.profiler`` is
just an interface to this tool.

There are two directives:

* ``timecall`` -> gives you the number of seconds per call.

Example::

 <configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:profiler="http://namespaces.plone.org/profiler"
    xmlns:five="http://namespaces.zope.org/five"
    xmlns:i18n="http://namespaces.zope.org/i18n">
   <profiler:timecall
        class="Products.CMFPlone.ActionsTool.ActionsTool"
        method="listFilteredActionsFor"
          />
  </configure>

This declaration will give you some information about the
``listFilteredActionsFor`` method.

If you start your Zope instance in the foreground, after startup you will
see::

 listFilteredActionsFor (.../eggs/Plone-3.3.5-py2.4.egg/Products/CMFPlone/ActionsTool.py:94):
    1 calls, 0.238 seconds (0.238 seconds per call)

* ``profile`` -> print the results of profiling.

Example:: 

  <configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:profiler="http://namespaces.plone.org/profiler"
    xmlns:five="http://namespaces.zope.org/five"
    xmlns:i18n="http://namespaces.zope.org/i18n">
    <profiler:profile
        class="Products.CMFPlone.ActionsTool.ActionsTool"
        method="listFilteredActionsFor"
        />
  </configure>

If you start your Zope instance in the foreground, after startup you will
see::

 *** PROFILER RESULTS ***
 listFilteredActionsFor (/Users/yboussard/.virtualenvs/dpldt/buildout/eggs/Plone-3.3.5-py2.4.egg/Products/CMFPlone/ActionsTool.py:94)
 function called 1 times

         228731 function calls (211122 primitive calls) in 1.730 CPU seconds

   Ordered by: cumulative time, internal time, call count
   List reduced from 871 to 40 due to restriction <40>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.730    1.730 profile:0(<unbound method ActionsTool.listFilteredActionsFor>)
        1    0.000    0.000    1.729    1.729 ActionsTool.py:94(listFilteredActionsFor)
        1    0.001    0.001    1.676    1.676 ActionsTool.py:44(listActionInfos)
  195/167    0.002    0.000    1.622    0.010 ActionInformation.py:197(__getitem__)
       18    0.001    0.000    1.612    0.090 Expression.py:40(__call__)
        6    0.000    0.000    1.221    0.204 ProfilerPatch.py:19(__patched_call__)
        6    0.000    0.000    1.221    0.203 expressions.py:214(__call__)
        6    0.000    0.000    1.221    0.203 Expressions.py:144(_eval)
        6    0.000    0.000    1.086    0.181 Expressions.py:108(render)
       33    0.000    0.000    0.868    0.026 RCompile.py:68(compileAndTuplize)
       33    0.001    0.000    0.867    0.026 RCompile.py:62(compile)
       10    0.000    0.000    0.767    0.077 FSObject.py:168(_updateFromFS)
        7    0.000    0.000    0.766    0.109 FSPythonScript.py:117(_readFile)
        7    0.000    0.000    0.765    0.109 FSPythonScript.py:255(_write)
       21    0.000    0.000    0.752    0.036 PythonScript.py:275(_makeFunction)
       21    0.001    0.000    0.751    0.036 PythonScript.py:232(_compile)
       21    0.000    0.000    0.746    0.036 PythonScript.py:229(_compiler)
       21    0.000    0.000    0.746    0.036 RCompile.py:75(compile_restricted_function)
      8/3    0.000    0.000    0.693    0.231 FSPythonScript.py:137(__call__)
     10/4    0.000    0.000    0.611    0.153 Bindings.py:331(_bindAndExec)
     10/4    0.001    0.000    0.608    0.152 FSPythonScript.py:144(_exec)
        1    0.000    0.000    0.568    0.568 flashupload.py:65(can_upload)
        1    0.000    0.000    0.560    0.560 flashupload.py:62(allowed_types)
      8/3    0.000    0.000    0.545    0.182 Bindings.py:311(__call__)
        2    0.000    0.000    0.515    0.258 ZRPythonExpr.py:66(call_with_ns)
        2    0.000    0.000    0.511    0.255 FSPythonScript.py:132(__render_with_namespace__)
        1    0.000    0.000    0.469    0.469 Script (Python):1(getAllowedTypes)
      319    0.003    0.000    0.396    0.001 Connection.py:749(setstate)
      319    0.009    0.000    0.393    0.001 Connection.py:769(_setstate)
        7    0.003    0.000    0.345    0.049 PythonScript.py:395(write)
       33    0.001    0.000    0.338    0.010 RCompile.py:53(_get_tree)
      319    0.005    0.000    0.321    0.001 serialize.py:603(setGhostState)
      319    0.005    0.000    0.314    0.001 serialize.py:593(getState)
 1289/638    0.023    0.000    0.301    0.000 :0(load)
  208/108    0.002    0.000    0.280    0.003 visitor.py:101(walk)
  208/108    0.002    0.000    0.278    0.003 visitor.py:59(preorder)
 3858/108    0.049    0.000    0.277    0.003 visitor.py:42(dispatch)
    56/33    0.000    0.000    0.276    0.008 pycodegen.py:241(getCode)
    56/33    0.002    0.000    0.276    0.008 pyassem.py:365(getCode)
        1    0.000    0.000    0.272    0.272 constraintypes.py:243(allowedContentTypes)

Options
=======

timecall
--------

``immediate``
    If you just want a summary at program termination, use ``False``.

profile
-------
 
``skip``
    If ``skip`` is > 0, the first ``skip`` calls to ``fn`` will not be
    profiled. (This is useful to let any caches get warmed up.)
 
``filename``
    If ``filename`` is specified, the profile stats will be stored in the
    named file. You can analyse it with the profiler tool or with
    ``pstats.Stats(filename)``.

``immediate``
    If ``immediate`` is ``False``, profiling results will be printed to
    ``sys.stdout`` on program termination.

``dirs``
    If ``dirs`` is ``False`` only the name of the file will be printed.
    Otherwise the full path is used.

``sort``
    ``sort`` can be a list of sort keys (defaulting to ``['cumulative',
    'time', 'calls']``).  The following keys are recognized::

        'calls'      -- call count
        'cumulative' -- cumulative time
        'file'       -- file name
        'line'       -- line number
        'module'     -- file name
        'name'       -- function name
        'nfl'        -- name/file/line
        'pcalls'     -- call count
        'stdname'    -- standard name
        'time'       -- internal time

``entries``
    ``entries`` limits the output to the first N entries.

