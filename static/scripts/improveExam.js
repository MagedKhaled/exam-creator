const handleRetryExamGenerator = (treeIndex) => {

    const url = '/create/retry/exam/';
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": '{{ csrf_token }}',
        },
        body: JSON.stringify({  
            'treeIndex': treeIndex,
        })
    })
    
};

