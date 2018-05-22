


def plotROC(probas_,test_y,label = 1):
    from scipy import interp
    from sklearn.metrics import roc_curve, auc

    ###############################################################################
    #ROC analysis
    # 分类，做ROC分析
    if label< 0 or label >= len(probas_[0]):
        print('roc error')
        return

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 0.1,100)
    # Compute ROC curve and area the curve
    # 通过roc_curve()函数，求出fpr和tpr，以及阈值
    fpr, tpr, thresholds = roc_curve(test_y, probas_[:,1],pos_label=label)
    mean_tpr += interp(mean_fpr, fpr, tpr)  # 对mean_tpr在mean_fpr处进行插值，通过scipy包调用interp()函数
    mean_tpr[0] = 0.0  # 初始处为0
    roc_auc = auc(fpr, tpr)
    # 画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
    plt.plot(fpr, tpr, lw=1, label='ROC  area = %0.2f)' % (roc_auc))

    # 画对角线
    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve ')
    plt.legend(loc="lower right")
    plt.show()
